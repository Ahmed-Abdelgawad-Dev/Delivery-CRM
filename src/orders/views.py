from django.shortcuts import render
from django.shortcuts import get_object_or_404
import datetime
from items.models import Item

from customers.models import Customer
from orders.models import Order, OrderItem






def order_list(request):
    # orders = Order.objects.filter(created__gt=datetime.date.today() - datetime.timedelta(days=1))
    orders = Order.objects.all()
    context = {'orders':orders}
    return render(request, 'orders/order_list.html', context)
    

def order_detail(request, id):
    order_items = OrderItem.objects.all()
    context = {'order_items': order_items}
    return render (request, 'orders/order_detail.html', {'order_items': order_items})

# def order_create(request):
#     return render(request, 'orders/order_create.html')
    