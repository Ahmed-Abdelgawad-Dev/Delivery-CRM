from django.db import models


class Customer(models.Model):
    first_name  = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name   = models.CharField(max_length=100)
    slug        =models.SlugField()
    mobile      = models.CharField(max_length=50)
    address     = models.TextField(null=False, blank=False)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        if not self.middle_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
    