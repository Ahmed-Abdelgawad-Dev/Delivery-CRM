from django.contrib import admin
from orders.models import Order, OrderItem
import datetime
from import_export import resources

from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter
from import_export.admin import ImportExportModelAdmin


from import_export.admin import ExportActionModelAdmin


class OrderItemAdmin2(admin.ModelAdmin):
    list_display = ["order", "id", "item", "quantity",  "created"]
    search_fields = ["order", "id", "item", "created",]
    list_filter = (
        ('created', DateRangeFilter),
        ('updated',DateTimeRangeFilter),
        ('id', NumericRangeFilter),
        #  "order", "item",
    )
    model = OrderItem


admin.site.register(OrderItem, OrderItemAdmin2)
# class OrderItemAdmin(admin.TabularInline):
#     list_display = ["order", "id", "item", "quantity", "price", "created"]
#     search_fields = ["order", "id", "item", "created",]
#     list_filter = (
#         ('created', DateRangeFilter),
#         ('updated',DateTimeRangeFilter),
#         ('id', NumericRangeFilter),
#          "order", "item",
#     )
#     model = OrderItem


class OrderAdmin(ExportActionModelAdmin):
    list_display = ["customer","id","customer", "active", "paid", "created"]
    list_filter = (
        ('id', NumericRangeFilter),
        ('created', DateRangeFilter),
        "customer", "active","paid", "delivered"
    )
    date_hierarchy = "created"
    search_fields = ["id", "customer__name", "customer__mobile"]
    # inlines = [OrderItemAdmin]

    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)

admin.site.register(Order, OrderAdmin)


# class OrderItemAdmin(admin.TabularInline):
#     list_display = ["order", "id", "item","quantity", "price", "created"]
#     list_filter = ["order", "id", "item", "created"]
#     search_fields = ["order", "id", "item", "created",]
#     model = OrderItem


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ["customer", "active", "id", "paid", "created", "delivered"]
#     list_filter = ["customer", "active", "id", "paid", "created", "delivered"]
#     date_hierarchy = "created"
#     search_fields = ["id", "customer__name", "customer__mobile"]
#     inlines = [OrderItemAdmin]


# admin.site.register(Order, OrderAdmin)
