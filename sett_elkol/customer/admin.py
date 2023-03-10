from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "gender", "phone_number", "country", "city"]
    list_filter = ["gender", "country", "city"]
    list_display_links = ["id", "pkid"]


admin.site.register(Customer, CustomerAdmin)
