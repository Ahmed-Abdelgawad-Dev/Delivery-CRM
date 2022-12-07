from django.views.generic import (
    CreateView, DetailView, ListView, UpdateView, DeleteView
)
from django.urls import reverse_lazy

from items.models import Item
from items.forms import ItemForm



class ItemListView(ListView):
    model               = Item
    template_name       = 'items/item_list.html'
    context_object_name = 'items_list'
    
    
class ItemDetailView(DetailView):
    model               = Item
    template_name       = 'items/item_detail.html'
    context_object_name = 'item'
    
class ItemCreateView(CreateView):
    model         = Item
    template_name = 'items/item_create.html'
    form_class    = ItemForm
    


class ItemUpdateView(UpdateView):
    model         = Item
    template_name = 'items/item_update.html'
    pk_url_kwarg = 'pk'
    form_class    = ItemForm


class ItemDeleteView(DeleteView):
    model         = Item
    template_name = 'items/item_delete.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'item'
    success_url         = reverse_lazy('item_list')
    