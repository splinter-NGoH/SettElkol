from django.urls import path

from sett_elkol.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    ActivateAccount,
    CustomTokenObtainPairView
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path("<str:uid>/<str:token>/", view=ActivateAccount.as_view(), name="activate"),
    path('auth/jwt/token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),

]
