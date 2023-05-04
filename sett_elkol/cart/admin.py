from django.contrib import admin

from . import models



class CartItemAdmin(admin.ModelAdmin):
    list_display = ["pkid", "meal", "item_name", "quantity", "price", "created_at"]
    list_display_links = ["pkid", "meal"]


admin.site.register(models.CartItem, CartItemAdmin)
