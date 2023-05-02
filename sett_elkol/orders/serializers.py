from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Order
# from carty.models import price
from sett_elkol.carty.serializers import CartItemSerializer

User = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    items = CartItemSerializer(many=True, read_only=True)
    # total_price = serializers.PrimaryKeyRelatedField(queryset=price.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'user', 'items',  'created_at']
        read_only_fields = ['id', 'items', 'created_at']






# from rest_framework import serializers
# from orders.models import Order
# from carty.serializers import CartItemSerializer

# class OrderSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True)

#     class Meta:
#         model = Order
#         fields = ['id', 'user', 'items', 'status', 'total', 'created_at']
#         read_only_fields = ['id', 'created_at']


# # from rest_framework import serializers
# # from .models import Order_Details , CartItem
# # class CartItemSerializer(serializers.ModelSerializer):
# #     meal = serializers.CharField(source = "meal.Meal.title")
# #     customer_user = serializers.CharField(source = "customer.user") 
# #     class Meta:
# #         model = CartItem
# #         fields = '__all__'
# # class OrderSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Order_Details
# #         fields = '__all__'
        
        




