from django.urls import path

from .views import create_article_rating_view

urlpatterns = [
    path("<str:meal_id>/", create_article_rating_view, name="rate-meal")
]