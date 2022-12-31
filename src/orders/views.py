from django.shortcuts import render
from orders.models import Order, OrderItem
from customers.forms import CustomerForm
from orders.forms import OrderItemForm
from items.forms import ItemForm
from items.models import Item
from django.forms import modelform_factory, modelformset_factory

def order_create(request):
    # customer=''
    # if request.method == "POST":
    #     form = CustomerForm(request.POST)
    #     form2 = OrderItemForm(request.POST)
    #     if form.is_valid():
    #         new_customer = form.save()
    #         customer=new_customer
    #     if customer != '':
    #         order = Order.objects.create(customer=customer, active=True)
    #         print('C U S T O M E R', customer, customer.id)
    #         print('O R D E R',order, order.id)
    # form = modelformset_factory(request.POST)
    formset = modelformset_factory(Item, ItemForm, fields=('name', 'price', 'category',), extra=5)
    if request.method == "POST":
        form = formset(request.POST)
        if form.is_valid():
            item = form.save()
            # print(item.name, item.price, item.category)

    context={"form":form}
    return render(request, 'orders/order_create.html', context)








def order_list(request):
    orders = Order.objects.filter(active=True)
    context = {"orders": orders}
    return render(request, "orders/order_list.html", context)

def order_detail(request, id):
    order_list = []
    orders = Order.objects.filter(active=True)
    order_items = OrderItem.objects.filter(order=id)
    for order in orders:
        for order_item in order_items:
            if order_item.order.id == order.id:
                order_list.append(order_item)

    context = {"order_list": order_list}
    print(context)
    return render(request, "orders/order_detail.html", context)
