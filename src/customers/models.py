
from django.db import models
from django.utils.text import slugify


class Customer(models.Model):
    name  = models.CharField(max_length=255)
    slug        =models.SlugField(blank=True)
    mobile      = models.CharField(max_length=50)
    address     = models.TextField(null=False, blank=False)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.name)


    
    def get_absolute_url(self):
        print(self.pk)
        from django.urls import reverse
        return reverse("customer_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.name)
       super(Customer, self).save(*args, **kwargs)