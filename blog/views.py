from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from pytils.translit import slugify

from blog.models import BlogArticle


class ArticleCreateView(CreateView):
    model = BlogArticle
    fields = ('title', 'text', 'is_published',)
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = BlogArticle
    fields = ('title', 'text', 'is_published',)

    def get_success_url(self):
        return reverse('blog:article', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = BlogArticle

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


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


def toggle_activity(request, pk):
    article = get_object_or_404(BlogArticle, pk=pk)
    article.is_published = not article.is_published
    article.save()

    return redirect(reverse('blog:blog_list'))
