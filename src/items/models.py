from django.db import models
from django.utils.translation import gettext_lazy as _

class Item(models.Model):
    class ItemFrom(models.TextChoices):
        MARKET          = 'MARKET',           _('Market')
        FRUIT_VEGETBLES = 'FRUIT_VEGETABLES', _('Fruit_Vegetables')
        OTHER           = 'OTHER',            _('Other')
    name     = models.CharField(max_length=100)
    price    = models.DecimalField(max_digits=6, decimal_places=2)
    source   = models.CharField(default=ItemFrom.OTHER,
                              choices=ItemFrom.choices, max_length=100)
    # merchant = models.ForeignKey(Merchant, on_delete=models.SET_NULL)
    created  = models.DateTimeField(auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name.lower())

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['name','source',]),]
    
