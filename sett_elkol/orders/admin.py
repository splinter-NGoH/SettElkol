from django.contrib import admin
from .models import Order

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ["pkid", "time", "date", "meal", "amount", "order_price","total_price"]
#     list_filter = ["time", "date", "meal", "total_price"]

admin.site.register(Order)

