from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg
from django.utils.translation import gettext_lazy as _

from sett_elkol.common.models import TimeStampedUUIDModel
from sett_elkol.rate.models import Rating

# from .read_time_engine import ArticleReadTimeEngine

User = get_user_model() 

class Category(TimeStampedUUIDModel):
    title = models.CharField(verbose_name=_("title"), max_length=250)
    slug = AutoSlugField(populate_from="title", always_update=True, unique=True)
    description = models.CharField(verbose_name=_("description"), max_length=255, null=True, blank=True)
    body = models.TextField(verbose_name=_("meal content"), null=True, blank=True)
    banner_image = models.ImageField(
        verbose_name=_("banner image"), null=True, blank=True
    )
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    def __str__(self):
        return f"{self.title}"
class Tag(TimeStampedUUIDModel):
    tag = models.CharField(max_length=80)
    slug = models.SlugField(db_index=True, unique=True)

    class Meta:
        ordering = ["tag"]

    def __str__(self):
        return self.tag


class Meal(TimeStampedUUIDModel):
    chef_user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("user"), related_name="meals"
    )
    title = models.CharField(verbose_name=_("title"), max_length=250)
    slug = AutoSlugField(populate_from="title", always_update=True, unique=True)
    description = models.CharField(verbose_name=_("description"), max_length=255)
    body = models.TextField(verbose_name=_("meal content"))
    banner_image = models.ImageField(
        verbose_name=_("banner image"), default="/customer_default.jpg"
    )
    tags = models.ManyToManyField(Tag, related_name="meals", null=True, blank=True)
    views = models.IntegerField(verbose_name=_("meal views"), default=0)
    price = models.IntegerField(verbose_name=_("price"), default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=_("category"), related_name="meals_of_category", blank=True, null=True
    )
    def __str__(self):
        return f"{self.chef_user.username}'s meal"

    @property
    def list_of_tags(self):
        tags = [tag.tag for tag in self.tags.all()]
        return tags

    # @property
    # def article_read_time(self):
    #     time_to_read = ArticleReadTimeEngine(self)
    #     return time_to_read.get_read_time()

    def get_average_rating(self):
        if Rating.objects.all().count() > 0:
            rating = (
                Rating.objects.filter(meal=self.pkid).all().aggregate(Avg("value"))
            )
            return round(rating["value__avg"], 1) if rating["value__avg"] else 0
        return 0


class MealViews(TimeStampedUUIDModel):
    ip = models.CharField(verbose_name=_("ip address"), max_length=250)
    meal = models.ForeignKey(
        Meal, related_name="meal_views", on_delete=models.CASCADE
    )

    def __str__(self):
        return (
            f"Total views on - {self.meal.title} is - {self.meal.views} view(s)"
        )

    class Meta:
        verbose_name = "Total views on Meal"
        verbose_name_plural = "Total Meal Views"

class ListofWarnings(TimeStampedUUIDModel):
    title = models.CharField(verbose_name=_("title"), max_length=250)
    slug = AutoSlugField(populate_from="title", always_update=True, unique=True)
    body = models.TextField(verbose_name=_("warning content"), null=True, blank=True)
    banner_image = models.ImageField(
        verbose_name=_("banner image"), null=True, blank=True
    )
    meal = models.ForeignKey(
        Meal, related_name="meal_warnings", on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = "List of Warning on Meal"
        verbose_name_plural = "List of Warnings"
    def __str__(self):
        return f"{self.title}"