from django.urls import path

from .views import (
    UpdateDelivaryAPIView,
    DelivaryListAPIView,
    DelivaryDetailAPIView,
    DelivaryProfileAPIView,
)

urlpatterns = [
    path(
        "Delivary/delivary_profile/", DelivaryProfileAPIView.as_view(), name="delivary-details"
    ),
    path("all/", DelivaryListAPIView.as_view(), name="all-delivarys"),
    path(
        "user/<str:username>/", DelivaryDetailAPIView.as_view(), name="Delivary-details"
    ),
    path(
        "update/<str:username>/", UpdateDelivaryAPIView.as_view(), name="Delivary-update"
    ),

]