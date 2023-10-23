from django.urls import path

from catalog.views import home_page, contact_info, product_details

urlpatterns = [
    path('', home_page),
    path('contacts', contact_info),
    path('products/<int:product_id>/', product_details, name='product_details'),
]