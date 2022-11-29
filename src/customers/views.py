from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from customers.models import Customer
from customers.forms import CustomerForm



class CustomerListView(ListView):
    model = Customer
    template_name='customers/customer_list.html'
    context_object_name = 'customers_list'
    
    
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer_detail'

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/customer_create.html'
    form_class = CustomerForm
