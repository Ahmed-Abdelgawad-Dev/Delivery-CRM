from django.urls import path
from .views import CustomerListView, CustomerDetailView


urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<slug:slug>/', CustomerDetailView.as_view(), name='customer_detail')
]
