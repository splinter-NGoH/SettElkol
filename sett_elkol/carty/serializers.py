from rest_framework import serializers
from django.contrib.auth import get_user_model
from sett_elkol.meal.models import Meal
from .models import CartItem

User = get_user_model()

class CartItemSerializer(serializers.ModelSerializer):
    meal = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all(), write_only=True)
    meal_name = serializers.CharField(source='meal.name', read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = CartItem
        # app_label = 'carty'
        fields = ( 'user', 'meal', 'meal_name', 'quantity', 'price', 'created_at', 'item_name')
        read_only_fields = ( 'created_at', 'user', 'item_name')


# from rest_framework import serializers
# from .models import CartItem

# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = '__all__'