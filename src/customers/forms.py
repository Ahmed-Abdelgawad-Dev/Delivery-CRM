from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['slug']
        # fields = ['name', 'mobile', 'address']    