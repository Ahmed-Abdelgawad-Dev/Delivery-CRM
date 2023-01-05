from django.db import models


class Customer(models.Model):
    name        = models.CharField(max_length=255, unique=True)
    mobile      = models.CharField(max_length=15, unique=True)
    address     = models.CharField(max_length=255)
    has_order   = models.BooleanField(default=False)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("customer_detail", kwargs={"pk": self.pk})

