from django.shortcuts import render
from orders.models import Order, OrderItem
from customers.models import Customer

def order_create(request):
    customer, mobile, order = '', '', ''
    if request.method == "GET":
        try:
            mobile = request.GET.get('mobile')
            if len(mobile) != 0:
                customer = Customer.objects.get(mobile=mobile)  
        except Customer.DoesNotExist:
            pass
    if request.method == "POST":
        customer = Customer.objects.create(
        name = request.POST.get('name'),
        mobile = request.POST.get('mobile'),
        address = request.POST.get('address'),
        )
        order = Order.objects.create(id=int(customer.id), active=True)
        
        

    context = {'customer': customer, 'order': order}
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
    return render(request, "orders/order_detail.html", context)
