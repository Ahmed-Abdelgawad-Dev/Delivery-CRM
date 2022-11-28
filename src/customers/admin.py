from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'first_name',
                    'last_name', 'mobile']
    search_fields = ['first_name', 'last_name']
    prepopulated_fields = {"slug": ("first_name","last_name",)}
admin.site.register(Customer, CustomerAdmin)
