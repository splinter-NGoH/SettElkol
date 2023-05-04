from django.shortcuts import render
from.models import CartItem
# Create your views here.
from rest_framework import filters, generics, permissions, status
import logging

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    CartItemSerializer,CartItemCreateSerializer
)
from sett_elkol.meal.models import Meal
from .models import CartItem
from .permissions import IsOwnerOrReadOnly
# class CartItemAPIView(generics.ListAPIView):
#     serializer_class = CartItemSerializer
#     # permission_classes = [
#     #     permissions.IsAuthenticated,
#     # ]
#     ordering_fields = ["created_at",]
#     def get_queryset(self):
#         user = self.request.user
#         return CartItem.objects.filter(user=user)
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = CartItemSerializer(queryset, many=True)
#         return Response(serializer.data)

class CartItemAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user.pkid)
        # x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(",")[0]
        # else:
        #     ip = request.META.get("REMOTE_ADDR")

        # if not MealViews.objects.filter(meal=meal, ip=ip).exists():
        #     MealViews.objects.create(meal=meal, ip=ip)
        #     meal.views += 1
        #     meal.save()

        serializer = CartItemSerializer(cart_items, context={"request": request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user.pkid)
        # x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        # if x_forwarded_for:
        #     ip = x_forwarded_for.split(",")[0]
        # else:
        #     ip = request.META.get("REMOTE_ADDR")

        # if not MealViews.objects.filter(meal=meal, ip=ip).exists():
        #     MealViews.objects.create(meal=meal, ip=ip)
        #     meal.views += 1
        #     meal.save()

        serializer = CartItemSerializer(cart_items, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CartItemCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CartItemCreateSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data["user"] = user.pkid
        try:
            meal = Meal.objects.get(id=data["meal"])

            cur_cart_item = CartItem.objects.get(user=request.user.pkid, meal=meal.pkid, status="incart")
            cur_cart_item.quantity +=1
            cur_cart_item.save()
            return Response({"id":cur_cart_item.id,
                             "meal":cur_cart_item.meal.id,
                             "quantity": cur_cart_item.quantity}, status=status.HTTP_201_CREATED)

        except CartItem.DoesNotExist:
            meal = Meal.objects.get(id=data["meal"])

            data["item_name"] = meal.title
            data["quantity"] = 1
            data["price"] = meal.price
            data["meal"] = meal.pkid
            serializer = self.serializer_class(data=data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class CartItemRemoveAPIView(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = CartItemCreateSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data["user"] = user.pkid
        meal = Meal.objects.get(id=data["meal"])
        try:
            cur_cart_item = CartItem.objects.get(user=request.user.pkid, meal=meal.pkid, status="incart")
            cur_cart_item.quantity -=1
            cur_cart_item.save()
            return Response({"cart_item_id":cur_cart_item.id,
                             "meal":cur_cart_item.meal.id,
                             "quantity": cur_cart_item.quantity}, status=status.HTTP_201_CREATED)

        except CartItem.DoesNotExist:
            raise NotFound


class CartItemDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = CartItem.objects.all()
    lookup_field = "id"
    def delete(self, request, *args, **kwargs):
        
        try:
            CartItem.objects.get(id=self.kwargs.get("id"), user=request.user.pkid).delete()
            return Response(data={"data":"successful"})

            # cart_item = CartItem.objasdsects.get(id=self.kwargs.get("id"), user=request.user)
        except CartItem.DoesNotExist:
            raise NotFound("That Cart Item does not exist in Cart")

        # delete_operation = self.destroy(request)
        # data = {}
        # if delete_operation:
        #     data["success"] = "Deletion was successful"

        # else:
        #     data["failure"] = "Deletion failed"

# class CartItemDeleteAPIView(generics.CreateAPIView):
#     permission_classes = [
#         permissions.IsAuthenticated,
#     ]
#     serializer_class = CartItemCreateSerializer

#     def create(self, request, *args, **kwargs):
#         user = request.user
#         data = request.data
#         data["user"] = user.pkid
#         meal = Meal.objects.get(id=data["meal"])
#         try:
#             cur_cart_item = CartItem.objects.get(user=request.user.pkid, meal=meal.pkid, status="incart")
#             cur_cart_item.quantity -=1
#             cur_cart_item.save()
#             return Response({"cart_item_id":cur_cart_item.id,
#                              "quantity": cur_cart_item.quantity}, status=status.HTTP_201_CREATED)

#         except CartItem.DoesNotExist:
#             raise NotFound

