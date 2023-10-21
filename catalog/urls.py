from django.urls import path

from catalog.views import home_page, contact_info, banana, potato, apple, step, pork

urlpatterns = [
    path('', home_page),
    path('contacts', contact_info),
    path('banana', banana),
    path('potato', potato),
    path('apple', apple),
    path('step', step),
    path('pork', pork)
]