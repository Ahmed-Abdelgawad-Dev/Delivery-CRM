from django.urls import path
from .views import (
    ItemListView, ItemDetailView, ItemCreateView,
    ItemUpdateView, ItemDeleteView
)


urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('create/', ItemCreateView.as_view(), name='item_create'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='item_update'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),
]
