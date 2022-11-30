from django.urls import path
from .views import (
    CustomerListView, CustomerDetailView, CustomerCreateView, 
    CustomerUpdateView, CustomerDeleteView
)


urlpatterns = [
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<slug:slug>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/update/<slug:slug>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/delete/<slug:slug>/', CustomerDeleteView.as_view(), name='customer_delete'),
]
