from django.urls import path
from orders.views import (
    order_list, order_detail, order_create,
    order_delete, order_status_toggler
)

urlpatterns = [
    path('', order_list, name='order_list'),
    path('<int:id>/change_status/', order_status_toggler, name='order_status_toggle'),
    path('<int:id>/detail/', order_detail, name='order_detail'),
    path('create_or_update/<int:id>/', order_create, name='order_create'),
    path('<int:id>/delete', order_delete, name='order_delete'),
]
