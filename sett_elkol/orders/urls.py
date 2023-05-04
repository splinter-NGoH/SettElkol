from django.urls import path
from .views import OrderCreateAPIView

urlpatterns = [
    path('order-add/', OrderCreateAPIView.as_view(), name='order-add'),
    # path('orders-details/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]



# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from orders.views import OrderList, OrderDetail

# app_name = 'orders'

# urlpatterns = [
#     path('', OrderList.as_view(), name='order-list'),
#     path('<int:pk>/', OrderDetail.as_view(), name='order-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

