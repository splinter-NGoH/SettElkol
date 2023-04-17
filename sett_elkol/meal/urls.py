from django.urls import path

from .views import (
    MealCreateAPIView,
    MealDeleteAPIView,
    MealDetailView,
    MealListAPIView,
    MealTrendingListAPIView,
    update_chef_api_view,
    CategoriesListAPIView,
    WarningListAPIView,
)

urlpatterns = [
    path("all/", MealListAPIView.as_view(), name="all-meals"),
    path("trending/", MealTrendingListAPIView.as_view(), name="all-trending"),
    path("create/", MealCreateAPIView.as_view(), name="create-meal"),
    path("details/<slug:slug>/", MealDetailView.as_view(), name="meal-detail"),
    path("delete/<slug:slug>/", MealDeleteAPIView.as_view(), name="delete-meal"),
    path("update/<slug:slug>/", update_chef_api_view, name="update-meal"),
    path("categories/", CategoriesListAPIView.as_view(), name="all-categories"),
    path("warnings/", WarningListAPIView.as_view(), name="all-warnings"),

]
