from django.urls import path
from . import views

urlpatterns = [
    path('', views.reports, name='reports'),
    path('orders_made_today/', views.orders_made_today, name='orders_made_today'),
    path('orders_made_today2/', views.orders_made_today2,
         name='orders_made_today2'),
]
