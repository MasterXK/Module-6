from django.shortcuts import render
from catalog.models import Product


def home(request):

    return render(request, 'catalog/home.html')


def contacts(request):

    return render(request, 'catalog/contacts.html')


def products(request):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list
    }

    return render(request, 'catalog/products.html', context)


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'object': product
    }

    return render(request, 'catalog/product_view.html', context)
