from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView

from blog.models import BlogArticle


class ArticleCreateView(CreateView):
    model = BlogArticle
    fields = ('title', 'text', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')


class ArticleUpdateView(UpdateView):
    model = BlogArticle
    fields = ('title', 'text', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    model = BlogArticle


class ArticleDeleteView(DeleteView):
    model = BlogArticle
    success_url = reverse_lazy('blog:blog_list')


class BlogDetailView(DetailView):
    model = BlogArticle

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()

        return self.object