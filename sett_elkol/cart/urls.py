from django.urls import path

from .views import (
    CartItemAPIView,
    CartItemCreateAPIView,
    CartItemRemoveAPIView,
    CartItemDeleteAPIView,

)

urlpatterns = [
    path("all_cart_items/", CartItemAPIView.as_view(), name="all-items"),
    path("add_to_cart/", CartItemCreateAPIView.as_view(), name="add-items"),
    path("remove_from_cart/", CartItemRemoveAPIView.as_view(), name="remove-items"),
    path("delete_Cart_item/<str:id>/", CartItemDeleteAPIView.as_view(), name="delete-items"),
   ]
