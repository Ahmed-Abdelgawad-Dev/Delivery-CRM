from django.forms import ModelForm
from orders.models import Order, OrderItem


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'
