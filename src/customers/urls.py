from django.urls import path
from customers.views import (
    CustomerListView, CustomerDetailView, CustomerCreateView, 
    CustomerUpdateView, CustomerDeleteView,
    find_customer

)


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('customer_create/', CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer_detail/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer_delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('customer_find/',find_customer, name='customer_find' )
]
