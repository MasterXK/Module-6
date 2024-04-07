from django.urls import path
from catalog.views import ContactsPageView, HomePageView, ProductListView, ProductDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ArticleCreateView.as_view(), name='create_article'),
]