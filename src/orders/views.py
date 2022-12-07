from django.shortcuts import render
from customers.models import Customer
from orders.models import Order, OrderItem
def create_order(request):
    # (get OR create) a customer by slug
    customers = customers.objects.all()
    # (get active OR create new) order
    orders = orders.objects.all()
    # add items to order
    # order_items