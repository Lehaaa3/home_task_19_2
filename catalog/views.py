from django.shortcuts import render

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



def banana(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
    }
    return render(request, 'catalog/banana.html', context)


def potato(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
    }
    return render(request, 'catalog/potato.html', context)


def pork(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
    }
    return render(request, 'catalog/pork.html', context)


def apple(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
    }
    return render(request, 'catalog/apple.html', context)


def step(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
    }
    return render(request, 'catalog/step.html', context)
