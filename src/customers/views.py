from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView
)
from django.urls import reverse, reverse_lazy

from customers.models import Customer
from customers.forms import CustomerForm



class CustomerListView(ListView):
    model               = Customer
    template_name       = 'customers/customer_list.html'
    context_object_name = 'customers_list'
    
    
class CustomerDetailView(DetailView):
    model               = Customer
    template_name       = 'customers/customer_detail.html'
    context_object_name = 'customer_detail'

class CustomerCreateView(CreateView):
    model         = Customer
    template_name = 'customers/customer_create.html'
    form_class    = CustomerForm


class CustomerUpdateView(UpdateView):
    model         = Customer
    template_name = 'customers/customer_update.html'
    form_class    = CustomerForm


class CustomerDeleteView(DeleteView):
    model               = Customer
    template_name       = 'customers/customer_delete.html'
    context_object_name = 'customer_'
    success_url         = reverse_lazy('customer_list')
