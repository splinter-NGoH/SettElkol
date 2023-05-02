from django.urls import path
from .views import CartItemList, CartItemDetail

urlpatterns = [
    path('cart-items/', CartItemList.as_view(), name='cart-item-list'),
    path('cart-items/<int:pk>/', CartItemDetail.as_view(), name='cart-item-detail'),
]







# from django.urls import path
# # from rest_framework.urlpatterns import format_suffix_patterns
# from .views import CartItemViewSet

# # app_name = 'cart'

# urlpatterns = [
#     path('items/', CartItemViewSet.as_view(), name='cartitem-list'),
#     path('items/<int:pk>/', CartItemViewSet.as_view(), name='cartitem-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)