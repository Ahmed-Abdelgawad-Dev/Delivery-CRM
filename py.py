def order_create(request):
    customer, mobile, order, formset = "", "", "", ""
    # Get a Customer
    if request.method == "GET":
        mobile = request.GET.get("mobile")
        if mobile is not None:
            try:
                customer = Customer.objects.get(mobile=mobile)
                if customer:
                    order = Order.objects.get(customer=customer)
            except:
                pass
    # Get a Customer
    if request.method == "GET":
        mobile = request.GET.get("mobile")
        if mobile is not None:
            try:
                customer = Customer.objects.get(mobile=mobile)
                if customer:
                    order = Order.objects.get(customer=customer)
            except:
                pass

    if request.method == "POST":
        customer = Customer.objects.create(
            name=request.POST.get("name"),
            mobile=request.POST.get("mobile"),
            address=request.POST.get("address"),
        )

        order = Order.objects.create(customer=customer, active=True)
        form = OrderItemForm(request.POST, instance=OrderItem)
        if form.is_valid():
            form.instance.item = Item
            form.instance.customer = customer
            form.save()

        order_item = OrderItem.objects.create(order=order, item=Item.ItemFrom)

    context = {"customer": customer, "order": order, "formset": formset, "form": form}
    return render(request, "orders/order_create.html", context)









if request.method == "POST":
        customer=None
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            new_customer = customer_form.save()
            print('C U S T O M E R: ->',customer, customer.id, customer.mobile)
        order = Order.objects.create(customer=customer, active=True)

    context = {"customer_form": customer_form}
    return render(request, 'orders/order_create.html', context)