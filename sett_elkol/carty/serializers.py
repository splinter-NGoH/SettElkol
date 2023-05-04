from rest_framework import serializers
from django.contrib.auth import get_user_model
from sett_elkol.meal.models import Meal
from .models import CartItem

User = get_user_model()


# from rest_framework import serializers
# from .models import CartItem

# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = '__all__'
class CartItemSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CartItem
        exclude = ["updated_at", "pkid"]
