from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from customers.models import Customer
from customers.forms import CustomerForm
from orders.models import Order, OrderItem
from django.forms import inlineformset_factory
from orders.forms import OrderItemForm, OrderForm




def order_create(request, id):
    customer = Customer.objects.get(id=id)
    order, Created = Order.objects.get_or_create(customer=customer)
    # order = Order.objects.get(customer=customer)
    ItemInlineFormSet = inlineformset_factory(
        Order, OrderItem, fields=('id', 'item', 'quantity',),
        extra=5, can_delete=True
        )
    if request.method == "POST":
        formset = ItemInlineFormSet(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
        return (redirect('order_detail', order.id))
    else:
        formset = ItemInlineFormSet(instance=order)
    return render(request, 'orders/order_create.html', {'formset': formset})


















def order_list(request):
    orders = Order.objects.filter(active=True)
    context = {"orders": orders}
    return render(request, "orders/order_list.html", context)

def order_detail(request, id):
    customer, order_list, order = None, [], None
    order = Order.objects.get(id=id)
    order_items = OrderItem.objects.filter(order=id)
    for order_item in order_items:
        if order_item.order.id == order.id:
            customer = order.customer
            order_list.append(order_item)
    context = {"order_list": order_list, "customer": customer, 'order': order}
    return render(request, "orders/order_detail.html", context)

