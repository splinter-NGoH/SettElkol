from django.contrib import admin

from . import models



class MealAdmin(admin.ModelAdmin):
    list_display = ["pkid", "chef_user", "slug", "views", "price"]
    list_display_links = ["pkid", "chef_user"]


admin.site.register(models.Meal, MealAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = ["pkid", "tag", "slug"]
    list_display_links = ["pkid", "tag"]


admin.site.register(models.Tag, TagAdmin)
