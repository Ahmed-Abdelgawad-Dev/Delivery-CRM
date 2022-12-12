from django.shortcuts import render
from django.shortcuts import get_object_or_404
from items.models import Item

from customers.models import Customer
from orders.models import Order, OrderItem
from orders.forms import OrderForm, OrderItemForm
from customers.forms import CustomerForm




def order_create(request):
    query=request.GET.get('query')
    print(f'--------------- {query} ----------------')
    result = Customer.objects.filter(mobile=query)
    
    context = {
        'result':result,
    }
    return render (request, 'orders/order_create.html', context)


def order_list(request):
    orders = Order.objects.filter(active=True)
    context = {'orders':orders}
    return render(request, 'orders/order_list.html', context)


def order_detail(request, id):
    order_list=[]
    orders = Order.objects.filter(active=True)
    order_items = OrderItem.objects.filter(order=id)
    for order in orders:
        for order_item in order_items:
            if order_item.order.id == order.id:
                order_list.append(order_item)
            
    context = {'order_list': order_list}
    return render (request, 'orders/order_detail.html', context)
