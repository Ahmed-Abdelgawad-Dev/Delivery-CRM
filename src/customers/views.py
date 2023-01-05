from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView
)

from customers.models import Customer
from customers.forms import CustomerForm
from orders.models import Order



class CustomerListView(ListView):
    model               = Customer
    template_name       = 'customers/customer_list.html'
    context_object_name = 'customers_list'



class CustomerDetailView(DetailView):
    model               = Customer
    template_name       = 'customers/customer_detail.html'
    context_object_name = 'customer_'

    def get_context_data(self, **kwargs):
        orders = Order.objects.all()
        context = {'orders': orders}
        return super().get_context_data(**context)


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


def find_customer(request):
    query=request.GET.get('query')
    result = Customer.objects.filter(mobile=query)
    context = {'result':result}
    return render (request, 'customers/customer_find.html', context)