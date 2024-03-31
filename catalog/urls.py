from django.urls import path
from catalog.views import home, contacts, products, product_view


urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path('products/', products),
    path('<int:pk>/', product_view),
]