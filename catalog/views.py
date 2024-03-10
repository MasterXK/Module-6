from django.shortcuts import render


def homepage(request):

    return render(request, 'catalog/homepage.html')


def contact_info(request):

    return render(request, 'catalog/contact_info.html')
