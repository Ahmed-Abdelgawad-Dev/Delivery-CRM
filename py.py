-------------------------------------------------------------------------------
def order_create(request, customer=None):
    customer = Customer.objects.get(id=1)
    order = Order.objects.get(customer=customer)
    OrderItemInlineFormSet = modelformset_factory(
        OrderItem, fields=('id', 'item', 'quantity',),
        extra=2, can_delete=True, min_num=1
        )
    if request.method == "POST":
        formset = OrderItemInlineFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            print([x for x in formset])
    else:
        formset = OrderItemInlineFormSet()
    return render(request, 'orders/order_create.html', {'formset': formset, 'order': order})
-------------------------------------------------------------------------------
