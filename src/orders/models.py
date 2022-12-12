from django.urls import reverse
from django.db import models
from customers.models import Customer
from items.models import Item


class Order(models.Model):
    customer  = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    created   = models.DateTimeField(auto_now_add=True)
    paid      = models.BooleanField(default=False)
    active    = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.name} | {self.id} | Active: {self.active} | Delivered: {self.delivered} | Paid: {self.paid}"

    class Meta:
        ordering = ["-created"]


class OrderItem(models.Model):
    order    = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    item     = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    price    = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item.name)

    class Meta:
        ordering = ["-created"]
