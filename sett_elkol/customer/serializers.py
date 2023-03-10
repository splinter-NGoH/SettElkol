from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    customer_photo = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Customer
        fields = [
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "id",
            "customer_photo",
            "phone_number",
            "about_me",
            "gender",
            "country",
            "age",
            "address",
            "university",
            "experience",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_customer_photo(self, obj):
        return obj.customer_photo.url


class UpdateCustomerSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Customer
        fields = [
            "phone_number",
            "customer_photo",
            "about_me",
            "gender",
            "country",
            "city",
            "age",
            "address",
            "university",
            "experience",
        ]

