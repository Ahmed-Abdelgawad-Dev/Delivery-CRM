from django.shortcuts import render
import datetime

from orders.models import Order, OrderItem


def reports(request):
    return render(request, 'reports/reports.html',)


def orders_made_today(request):
    today = datetime.date.today()
    year, month, day = today.year, today.month, today.day
    orders = OrderItem.objects.filter(created__year=year,
                                      created__month=month, created__day=day)
    total_price = sum([item.item.price*item.quantity for item in orders])
    return render(request, 'reports/orders_made_today.html', {"orders": orders, 'total_price': total_price})
