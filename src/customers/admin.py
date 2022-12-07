from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display  = ['name', 'id', 'mobile', 'has_order', 'created', 'updated']
    search_fields = ['name', 'id', 'mobile', 'has_order', 'created', 'updated']
    list_filter   = ['name', 'id', 'mobile', 'has_order', 'created', 'updated']
    # prepopulated_fields = {"slug": ("name",)}
admin.site.register(Customer, CustomerAdmin)
