from django.db import models
from items.models import Item
from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-created"]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, editable=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.item.name)

    class Meta:
        ordering = ["-created"]
