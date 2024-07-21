from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, contacts, products_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', product_list, name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', products_detail, name='product_detail')
]
