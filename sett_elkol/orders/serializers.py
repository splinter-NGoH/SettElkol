from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import OrderItems
# from carty.models import price
# from sett_elkol.carty.serializers import CartItemSerializer

User = get_user_model()

class OrderCreateSerializer(serializers.ModelSerializer): 
    banner_image = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = OrderItems
        exclude = ["updated_at", "pkid"]

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def get_banner_image(self, obj):
        return obj.banner_image.url





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
        
        




