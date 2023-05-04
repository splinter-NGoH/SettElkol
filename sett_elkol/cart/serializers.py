from rest_framework import serializers
from django.contrib.auth import get_user_model
from sett_elkol.meal.models import Meal
from .models import CartItem

User = get_user_model()
class CartItemSerializer(serializers.ModelSerializer): 
    meal_id = serializers.CharField(source="meal.id")
    class Meta:
        model = CartItem
        fields = ["id",
                    "pkid",
                    "user",
                    "meal_id",
                    "meal",
                    "item_name",
                    "quantity",
                    "price",
                    "status",
                    "created_at"]


# from rest_framework import serializers
# from .models import CartItem

# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = '__all__'


class CartItemCreateSerializer(serializers.ModelSerializer): 
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        exclude = ["updated_at", "pkid"]

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

