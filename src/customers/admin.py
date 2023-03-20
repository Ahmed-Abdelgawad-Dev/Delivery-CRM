from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter, NumericRangeFilter
from django.contrib import admin
from .models import Customer
import datetime
from django.contrib.admin import DateFieldListFilter
from import_export.admin import ExportActionModelAdmin


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'mobile', 'has_order', 'created', 'updated']
    search_fields = ['name', 'id', 'mobile', 'has_order', 'created', 'updated']
    list_filter = (
        ('created', DateRangeFilter),
        ('updated',DateTimeRangeFilter),
        ('id', NumericRangeFilter),
         'name', 'id', 'mobile', 'has_order', 'created', 'updated'
    )


    def get_rangefilter_created_at_default(self, request):
        return (datetime.date.today, datetime.date.today)

admin.site.register(Customer, CustomerAdmin)
