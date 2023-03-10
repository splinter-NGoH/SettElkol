from django.urls import path
from .views import CustomRegistrationView
urlpatterns = [
    path("register/", CustomRegistrationView.as_view({'post': 'create'})),

]
