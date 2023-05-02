from django.urls import path

from .views import (
    CustomerDetailAPIView,
    CustomerListAPIView,
    UpdateCustomerAPIView,
    CustomerProfileAPIView,
)  

urlpatterns = [
    path(
        "customer_profile/customer_profile/", CustomerProfileAPIView.as_view(), name="Customer-details"
    ),
    path("all_customer/", CustomerListAPIView.as_view(), name="all-Customers"),
    path(
        "customer/<str:username>/", CustomerDetailAPIView.as_view(), name="Customer-details"
    ),
    path(
        "update_customer/<str:username>/", UpdateCustomerAPIView.as_view(), name="Customer-update"
    ),

]
