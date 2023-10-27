from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contact_info, ProductDetailView, ProductListView
app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contact_info, name='contact_info'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
]