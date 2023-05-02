# from multiprocessing import context
# from unicodedata import name

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

# from authors_api.settings.production import DEFAULT_FROM_EMAIL

from .exceptions import  NotYourCustomer
from .models import Customer
from .pagination import CustomerPagination
from .renderers import CustomerJSONRenderer, CustomersJSONRenderer
from .serializers import  CustomerSerializer, UpdateCustomerSerializer

User = get_user_model() 


class CustomerListAPIView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Customer.objects.all()
    renderer_classes = (CustomersJSONRenderer,)
    pagination_class = CustomerPagination


class CustomerDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.select_related("user")
    serializer_class = CustomerSerializer
    renderer_classes = (CustomerJSONRenderer,)

    def retrieve(self, request, username, *args, **kwargs):
        try:
            customer = self.queryset.get(user__username=username)
        except Customer.DoesNotExist:
            raise NotFound("A Customer with this username does not exist")

        serializer = self.serializer_class(customer, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerProfileAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.select_related("user")
    serializer_class = CustomerSerializer
    renderer_classes = (CustomerJSONRenderer,)

    def retrieve(self, request, *args, **kwargs):
        try:
            customer = self.queryset.get(user=request.user)
        except Customer.DoesNotExist:
            raise NotFound("A Customer with this username does not exist")

        serializer = self.serializer_class(customer, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateCustomerAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Customer.objects.select_related("user")
    renderer_classes = [CustomerJSONRenderer]
    serializer_class = UpdateCustomerSerializer

    def patch(self, request, username):
        try:
            self.queryset.get(user__username=username)
        except Customer.DoesNotExist:
            raise NotFound("A Customer with this username does not exist")

        user_name = request.user.username
        if user_name != username:
            raise NotYourCustomer

        data = request.data
        serializer = UpdateCustomerSerializer(
            instance=request.user.customer, data=data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

