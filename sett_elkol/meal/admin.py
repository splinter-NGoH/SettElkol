from django.contrib import admin

from . import models



class MealAdmin(admin.ModelAdmin):
    list_display = ["pkid", "chef_user", "slug", "views", "price"]
    list_display_links = ["pkid", "chef_user"]


admin.site.register(models.Meal, MealAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pkid", "title", "slug", "description"]
    list_display_links = ["pkid", "title"]


admin.site.register(models.Category, CategoryAdmin)
class WarningsAdmin(admin.ModelAdmin):
    list_display = ["pkid", "title", "slug", "body"]
    list_display_links = ["pkid", "title"]


admin.site.register(models.ListofWarnings, WarningsAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ["pkid", "tag", "slug"]
    list_display_links = ["pkid", "tag"]


admin.site.register(models.Tag, TagAdmin)
