from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    list_display = ["order", "id", "item","quantity", "price", "created"]
    list_filter = ["order", "id", "item", "created"]
    search_fields = ["order", "id", "item", "created",]
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "active", "id", "paid", "created", "delivered"]
    list_filter = ["customer", "active", "id", "paid", "created", "delivered"]
    date_hierarchy = "created"
    search_fields = ["id", "customer__name"]
    inlines = [OrderItemAdmin]


admin.site.register(Order, OrderAdmin)
