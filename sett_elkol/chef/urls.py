from django.urls import path

from .views import (
    ChefDetailAPIView,
    ChefListAPIView,
    UpdateChefAPIView,
    ChefProfileAPIView,
)

urlpatterns = [
    path(
        "chef/chef_profile/", ChefProfileAPIView.as_view(), name="Chef-details"
    ),
    path("all/", ChefListAPIView.as_view(), name="all-Chefs"),
    path(
        "user/<str:username>/", ChefDetailAPIView.as_view(), name="Chef-details"
    ),
    path(
        "update/<str:username>/", UpdateChefAPIView.as_view(), name="Chef-update"
    ),

]
