from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django_countries.serializer_fields import CountryField

User = get_user_model()

class CreateUserSerializer(UserCreateSerializer):
    country = CountryField(name_only=True)
    full_name = serializers.SerializerMethodField(read_only=True)
 
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
                "id", 
                "username",
                "email",
                "first_name",
                "last_name",
                "full_name",
                "country",
                "gender",
                "city",
                "user_type",
                "password",
                ]

    def get_full_name(self, obj):
        first_name = obj.first_name.title()
        last_name = obj.last_name.title()
        return f"{first_name} {last_name}"

class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "gender",
            "phone_number",
            "profile_photo",
            "country",
            "city",
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)
        if instance.is_superuser:
            representation["admin"] = True
        return representation


