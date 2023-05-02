from rest_framework import serializers

from sett_elkol.meal.models import Meal, MealViews, ListofWarnings, Category
# from sett_elkol.comments.serializers import CommentListSerializer
# from sett_elkol.ratings.serializers import RatingSerializer

from .custom_tag_field import TagRelatedField
from sett_elkol.rate.serializers import RatingSerializer


class MealViewsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = MealViews
        exclude = ["updated_at", "pkid"]

class WarningSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListofWarnings
        exclude = ["updated_at", "pkid"]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ["updated_at", "pkid"]
class MealSerializer(serializers.ModelSerializer):
    chef_info = serializers.SerializerMethodField(read_only=True)
    banner_image = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    num_ratings = serializers.SerializerMethodField()
    average_rating = serializers.ReadOnlyField(source="get_average_rating")
    category = serializers.CharField(source="category.slug")
    list_of_warnings = serializers.SerializerMethodField()
    # likes = serializers.ReadOnlyField(source="article_reactions.likes")
    # dislikes = serializers.ReadOnlyField(source="article_reactions.dislikes")
    tagList = TagRelatedField(many=True, required=False, source="tags")
    # comments = serializers.SerializerMethodField()
    # num_comments = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField() 

    def get_banner_image(self, obj):
        return obj.banner_image.url

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def get_chef_info(self, obj):
        return {
            "username": obj.chef_user.username,
            "fullname": obj.chef_user.get_full_name,
            "email": obj.chef_user.email,
            "about_me": obj.chef_user.chef.about_me,
            "chef_photo": obj.chef_user.chef.chef_photo.url,    
        }

    def get_ratings(self, obj):
        reviews = obj.meal_ratings.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data
    def get_list_of_warnings(self, obj):
        warnings = obj.meal_warnings.all()
        serializer = WarningSerializer(warnings, many=True)
        return serializer.data
    def get_num_ratings(self, obj):
        num_reviews = obj.meal_ratings.all().count()
        return num_reviews

    # def get_comments(self, obj):
    #     comments = obj.comments.all()
    #     serializer = CommentListSerializer(comments, many=True)
    #     return serializer.data

    # def get_num_comments(self, obj):
    #     num_comments = obj.comments.all().count()
    #     return num_comments

    class Meta:
        model = Meal
        fields = [
            "id",
            "title",
            "slug",
            "price",
            "tagList",
            "description",
            "body",
            "category",
            "banner_image",
            "chef_info",
            "list_of_warnings",
            "views",
            "ratings",
            "num_ratings",
            "average_rating",
            "created_at", 
            "updated_at",
        ]


class MealCreateSerializer(serializers.ModelSerializer): 
    tags = TagRelatedField(many=True, required=False)
    banner_image = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Meal
        exclude = ["updated_at", "pkid"]

    def get_created_at(self, obj):
        now = obj.created_at
        formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date

    def get_banner_image(self, obj):
        return obj.banner_image.url


class MealUpdateSerializer(serializers.ModelSerializer):
    tags = TagRelatedField(many=True, required=False)
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Meal
        fields = ["title", "description", "body", "banner_image", "tags","price", "updated_at"]

    def get_updated_at(self, obj):
        then = obj.updated_at
        formatted_date = then.strftime("%m/%d/%Y, %H:%M:%S")
        return formatted_date
