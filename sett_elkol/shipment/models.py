# from django.db import models
# from django.contrib.auth.models import User
# from carty.models import CartItem
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Shipment(models.Model):
#     STATUS_CHOICES = [
#         ('coocking', 'coocking'),
#         ('shipped', 'Shipped'),
#         ('delivered', 'Delivered'),
#     ]
#     cart_items = models.ManyToManyField(CartItem, related_name='shipments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='coocking')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Shipment #{self.pk}'