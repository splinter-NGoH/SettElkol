from django.urls import path

from .views import (
    CartItemAPIView,
    CartItemCreateAPIView,

)

urlpatterns = [
    path("all_cart_items/", CartItemAPIView.as_view(), name="all-items"),
    path("add_to_cart/", CartItemCreateAPIView.as_view(), name="add-items"),
   ]
