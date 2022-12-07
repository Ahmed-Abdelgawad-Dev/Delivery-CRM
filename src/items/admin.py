from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'id', 'price', 'created', 'updated']
    list_filter  = ['name', 'category', 'id', 'price', 'created', 'updated']
    list_editable = ['price'] 
admin.site.register(Item, ItemAdmin)