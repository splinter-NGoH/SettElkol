from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from .models import Chef


class ChefSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name") 
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    chef_photo = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Chef
        fields = [
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "id",
            "chef_photo",
            "phone_number",
            "about_me",
            "gender",
            "country",
            "city",
            "age",
            "address",
            "university",
            "experience",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = ""
        if obj.user.last_name:
            last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_chef_photo(self, obj):
        return obj.chef_photo.url


class UpdateChefSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Chef
        fields = [
            "phone_number",
            "chef_photo",
            "about_me",
            "gender",
            "country",
            "city",
            "age",
            "address",
            "university",
            "experience",
        ]

