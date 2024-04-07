from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Product, BlogArticle
from django.views.generic import ListView, DeleteView, DetailView, TemplateView, CreateView


class HomePageView(TemplateView):
    template_name = "catalog/home.html"


class ContactsPageView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ArticleCreateView(CreateView):
    model = BlogArticle
    fields = ('title', 'text', 'preview',)
    success_url = reverse_lazy('catalog/home.html')