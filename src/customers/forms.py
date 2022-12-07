from django.forms import ModelForm
from customers.models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ['slug']