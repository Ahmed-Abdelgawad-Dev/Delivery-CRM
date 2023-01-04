from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from customers.forms import CustomerForm
from orders.forms import OrderItemForm
from customers.models import Customer
from orders.models import Order, OrderItem
from django.views.generic import TemplateView
from items.forms import ItemForm
from items.models import Item
from django.forms import modelform_factory, modelformset_factory, inlineformset_factory
from django.views.decorators.csrf import csrf_exempt
from customers.views import find_customer
from django.views.generic import CreateView





def order_create(request, customer=None):
    customer = Customer.objects.get(id=1)
    order = Order.objects.get(customer=customer)
    ItemInlineFormSet = inlineformset_factory(
        Order, OrderItem, fields=('id', 'item', 'quantity',),
        extra=1, can_delete=True
        )
    if request.method == "POST":
        formset = ItemInlineFormSet(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            print([x for x in formset])
    else:
        formset = ItemInlineFormSet(instance=order)
    return render(request, 'orders/order_create.html', {'formset': formset})


















def order_list(request):
    orders = Order.objects.filter(active=True)
    context = {"orders": orders}
    return render(request, "orders/order_list.html", context)

def order_detail(request, id):
    customer=None
    order_list = []
    # Will be applied later on.
    # orders = Order.objects.filter(active=True)
    orders = Order.objects.all()
    order_items = OrderItem.objects.filter(order=id)
    for order in orders:
        for order_item in order_items:
            if order_item.order.id == order.id:
                customer = (order.customer)
                order_list.append(order_item)

    context = {"order_list": order_list, "customer": customer}
    return render(request, "orders/order_detail.html", context)
