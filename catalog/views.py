from django.shortcuts import render
from django.views.generic import DetailView, ListView

from catalog.models import Product


def contact_info(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact_info.html', context)


# def home_page(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'Главная'
#     }
#     return render(request, 'catalog/home_page.html', context)

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
