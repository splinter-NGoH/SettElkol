from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from .models import Deliv



class DelivarySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    Delivary_photo = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Deliv
        fields = [
            "username",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "id",
            "delivary_photo",
            "phone_number",
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

    def get_delivary_photo(self, obj):
        return obj.Deliv_photo.url


class UpdateDelivarySerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Deliv
        fields = [
            "phone_number",
            "delivary_photo",
            "gender",
            "country",
            "city",
            "age",
            "address",
            "university",
            "experience",
        ]

