from django.urls import path
from .views import (
    CustomerListView, CustomerDetailView, CustomerCreateView
)


urlpatterns = [
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<slug>/', CustomerDetailView.as_view(), name='customer_detail'),
]
