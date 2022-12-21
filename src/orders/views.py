from django.shortcuts import render
from orders.models import Order, OrderItem
from customers.models import Customer

def order_create(request):
    customer, mobile, order = '', '', ''
    # Get customer info from DB if found.
    if request.method == "GET":
        try:
            mobile = request.GET.get('mobile')
            if mobile is not None:
                try:
                    customer = Customer.objects.get(mobile=mobile)
                    order = Order.objects.get(customer=customer)
                except:
                    order = Order.objects.create(customer=customer, active=True)        
        except Customer.DoesNotExist:
            pass
    # Create customer instead using the user input
    if request.method == "POST":
        customer = Customer.objects.create(
        name = request.POST.get('name'),
        mobile = request.POST.get('mobile'),
        address = request.POST.get('address'),
        )
        order = Order.objects.create(customer=customer, active=True)
    
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
    print(context)
    return render(request, "orders/order_detail.html", context)
