from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home_page(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home_page.html', context)


def contact_info(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact_info.html', context)


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'object': product,
    }
    return render(request, 'catalog/product_details.html', context)
