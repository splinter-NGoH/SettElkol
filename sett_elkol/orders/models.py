from django.db import models
from django.contrib.auth.models import User
# from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from sett_elkol.common.models import TimeStampedUUIDModel
# from rest_framework.authtoken.models import Token
from sett_elkol.cart.models import CartItem
User = get_user_model() 

class OrderDetails(TimeStampedUUIDModel):
    STATUS_CHOICES = (
        ('payed', 'payed'),
        ('unpayed', 'unpayed')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_oreders")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='unpayed')
    total_price = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f"Order for user #{self.user.username}"



class OrderItems(TimeStampedUUIDModel):
    parent = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, related_name="parent_items")
    cartItem = models.ForeignKey(CartItem, on_delete=models.CASCADE, related_name="item_code")
    rate = models.DecimalField(decimal_places=2, max_digits="20")
    quantity = models.IntegerField()
    banner_image = models.ImageField()

    def __str__(self):
        return f"Order #{self.cartItem}"

    # def save(self, *args, **kwargs):
    #     self.total = sum(CartItem.quantity * CartItem.price for item in self.items.all())


# # class CartItem(TimeStampedUUIDModel):
# #     class MealStatus(models.TextChoices):
# #         incart = "incart", _("incart")
# #         outcart = "outcart", _("outcart")
        
# #     customer = models.ForeignKey(
# #         User , related_name="user_cart_item", on_delete=models.CASCADE
# #     )
# #     meal = models.ForeignKey(
# #         Meal , related_name="meal_cart_item", on_delete=models.CASCADE
# #     )
# #     status = models.CharField(
# #         verbose_name=_("status"),
# #         choices=MealStatus.choices,
# #         default=MealStatus.incart,
# #         max_length=20,
# #     )
# #     price = models.FloatField()
# #     quantaties = models.IntegerField()
    
# # class Order_Details(TimeStampedUUIDModel): 
# #     class ReciptStatus(models.TextChoices):
# #         canceled = "canceled", _("canceled")
# #         payed = "payed", _("payed")
# #         unpayed = "unpayed", _("unpayed")
    
    
# #     cart_item = models.models.ManyToManyField("CartItem", verbose_name=_("cart_item"))
# #     quantity = models.IntegerField()
# #     price = models.DecimalField(max_digits=10, decimal_places=2)
    
# #     total_price = price * quantaties
# #     status = models.CharField(
# #         verbose_name=_("status"),
# #         choices=ReciptStatus.choices,
# #         default=ReciptStatus.canceled,
# #         max_length=20,
# #     )
    
    
 
 
# #  from rest_framework import generics, mixins, status
# # from rest_framework.permissions import IsAuthenticated
# # from rest_framework.response import Response
# # from orders.models import Order
# # from orders.serializers import OrderSerializer
# # from carts.models import CartItem

# # class OrderList(generics.ListCreateAPIView):
# #     serializer_class = OrderSerializer
# #     permission_classes = [IsAuthenticated]

# #     def get_queryset(self):
# #         return Order.objects.filter(user=self.request.user)

# #     def perform_create(self, serializer):
# #         items = serializer.validated_data.get('items')
# #         if not items:
# #             return Response({'error': 'Cannot create an order without items.'}, status=status.HTTP_400_BAD_REQUEST)
# #         total = sum(item.quantity * item.price for item in items)
# #         serializer.save(user=self.request.user, total=total)

# # class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Order.objects.all()
# #     serializer_class = OrderSerializer
# #     permission_classes = [IsAuthenticated]

# #     def destroy(self, request, *args, **kwargs):
# #         instance = self.get_object()
# #         instance.items.update(status='incart')
# #         return super().destroy(request, *args, **kwargs)   
