from xhtml2pdf import pisa
from io import BytesIO
import io
from django.shortcuts import render
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from datetime import date
from django.utils import timezone
import datetime

from orders.models import Order, OrderItem


def reports(request):
    return render(request, 'reports/reports.html',)


def orders_made_today(request):
    orders = OrderItem.objects.all()
    return render(request, 'reports/orders_made_today.html', {"orders": orders})

def orders_made_today2(request):
    orders = OrderItem.objects.all()
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
    txt = c.beginText()
    txt.setTextOrigin(inch, inch)
    txt.setFont("Helvetica", 15)
    lines = []
    for order in orders:
        lines.append(str(order.order.id))
        lines.append(str(order.order.customer.name))
        lines.append(str(order.order.created))
        lines.append(
            '-----------------------------------------------------------------------'
        )
    for line in lines:
        txt.textLine(line)
    c.drawText(txt)
    c.showPage()
    c.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="orders_made_today.pdf")
