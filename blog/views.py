from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, TemplateView, CreateView

from blog.models import BlogArticle


class ArticleCreateView(CreateView):
    model = BlogArticle
    fields = ('title', 'text',)
    success_url = reverse_lazy('blog:article')


class BlogListView(ListView):
    model = BlogArticle


class BlogDetailView(DetailView):
    model = BlogArticle
