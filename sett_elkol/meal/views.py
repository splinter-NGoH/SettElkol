import logging

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from sett_elkol.meal.models import Meal, MealViews, Category, ListofWarnings

from .exceptions import UpdateMeal, CreateMeal, UpdateMealChef
from .filters import MealFilter
from .pagination import MealPagination
from .permissions import IsOwnerOrReadOnly
from .renderers import MealJSONRenderer, MealsJSONRenderer
from .serializers import (
    MealCreateSerializer,
    MealSerializer,
    MealUpdateSerializer,
    CategorySerializer,
    WarningSerializer,
)
from sett_elkol.users.models import User

User = get_user_model()

logger = logging.getLogger(__name__)


class WarningListAPIView(generics.ListAPIView):
    serializer_class = WarningSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    queryset = ListofWarnings.objects.all()
    # renderer_classes = (MealsJSONRenderer,)
    pagination_class = MealPagination
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_class = MealFilter
    ordering_fields = ["created_at"]

class CategoriesListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    queryset = Category.objects.all()
    # renderer_classes = (MealsJSONRenderer,)
    pagination_class = MealPagination
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_class = MealFilter
    ordering_fields = ["created_at"]

class MealListAPIView(generics.ListAPIView):
    serializer_class = MealSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    queryset = Meal.objects.all()
    renderer_classes = (MealsJSONRenderer,)
    pagination_class = MealPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MealFilter
    ordering_fields = ["created_at", "username"]

class MealTrendingListAPIView(generics.ListAPIView):
    serializer_class = MealSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    queryset = Meal.objects.all()
    renderer_classes = (MealsJSONRenderer,)
    pagination_class = MealPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MealFilter
    ordering_fields = ["-views"]


class MealCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = MealCreateSerializer
    renderer_classes = [MealJSONRenderer]

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.user_type != User.UserType.CHEF:
            raise CreateMeal
        data = request.data
        data["chef_user"] = user.pkid
        serializer = self.serializer_class(data=data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(
            f"chef_user {serializer.data.get('title')} created by {user.username}"
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MealDetailView(APIView):
    renderer_classes = [MealJSONRenderer]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, slug):
        meal = Meal.objects.get(slug=slug)
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        if not MealViews.objects.filter(meal=meal, ip=ip).exists():
            MealViews.objects.create(meal=meal, ip=ip)
            meal.views += 1
            meal.save()

        serializer = MealSerializer(meal, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PATCH"])
@permission_classes([permissions.IsAuthenticated])
def update_chef_api_view(request, slug):
    try:
        meal = Meal.objects.get(slug=slug)
    except Meal.DoesNotExist:
        raise NotFound("That meal does not exist in our catalog")

    user = request.user
    if meal.chef_user != user:
        raise UpdateMeal
    if user.user_type != User.UserType.CHEF:
        raise UpdateMealChef
    if request.method == "PATCH":
        data = request.data
        serializer = MealUpdateSerializer(meal, data=data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class MealDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Meal.objects.all()
    lookup_field = "slug"

    def delete(self, request, *args, **kwargs):
        try:
            meal = Meal.objects.get(slug=self.kwargs.get("slug"))
        except Meal.DoesNotExist:
            raise NotFound("That meal does not exist in our catalog")

        delete_operation = self.destroy(request)
        data = {}
        if delete_operation:
            data["success"] = "Deletion was successful"

        else:
            data["failure"] = "Deletion failed"

        return Response(data=data)
