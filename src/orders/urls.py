from django.urls import path
from orders.views import (
    order_list, order_detail, order_create,
)

urlpatterns = [
    path('', order_list, name='order_list'),
    path('<int:id>', order_detail, name='order_detail'),
    path('order_create/', order_create, name='order_create'),
]
