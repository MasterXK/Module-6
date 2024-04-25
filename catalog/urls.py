from django.urls import path
from catalog.views import ContactsPageView, HomePageView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('product<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/product<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/product<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
