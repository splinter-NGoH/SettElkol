from django.contrib import admin

from .models import Rating


class RatingAdmin(admin.ModelAdmin):
    list_display = ["meal", "rated_by", "value"]


admin.site.register(Rating, RatingAdmin)