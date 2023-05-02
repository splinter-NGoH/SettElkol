from django.urls import path, include
from payment_api.views import PaymentListCreateView, PaymentRetrieveUpdateDeleteView

urlpatterns = [
    path('api/', include([
        path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
        path('payments/<int:pk>/', PaymentRetrieveUpdateDeleteView.as_view(), name='payment-retrieve-update-delete'),
    ])),
]