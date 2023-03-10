# from multiprocessing import context
# from unicodedata import name

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

# from authors_api.settings.production import DEFAULT_FROM_EMAIL

from .exceptions import  NotYourChef
from .models import Chef
from .pagination import ChefPagination
from .renderers import ChefJSONRenderer, ChefsJSONRenderer
from .serializers import  ChefSerializer, UpdateChefSerializer

User = get_user_model()


class ChefListAPIView(generics.ListAPIView):
    serializer_class = ChefSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Chef.objects.all()
    renderer_classes = (ChefsJSONRenderer,)
    pagination_class = ChefPagination


class ChefDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Chef.objects.select_related("user")
    serializer_class = ChefSerializer
    renderer_classes = (ChefJSONRenderer,)

    def retrieve(self, request, username, *args, **kwargs):
        try:
            chef = self.queryset.get(user__username=username)
        except Chef.DoesNotExist:
            raise NotFound("A Chef with this username does not exist")

        serializer = self.serializer_class(chef, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ChefProfileAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Chef.objects.select_related("user")
    serializer_class = ChefSerializer
    renderer_classes = (ChefJSONRenderer,)

    def retrieve(self, request, *args, **kwargs):
        try:
            chef = self.queryset.get(user=request.user)
        except Chef.DoesNotExist:
            raise NotFound("A Chef with this profile does not exist")

        serializer = self.serializer_class(chef, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateChefAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Chef.objects.select_related("user")
    renderer_classes = [ChefJSONRenderer]
    serializer_class = UpdateChefSerializer

    def patch(self, request, username):
        try:
            self.queryset.get(user__username=username)
        except Chef.DoesNotExist:
            raise NotFound("A Chef with this username does not exist")

        user_name = request.user.username
        if user_name != username:
            raise NotYourChef

        data = request.data
        serializer = UpdateChefSerializer(
            instance=request.user.chef, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

