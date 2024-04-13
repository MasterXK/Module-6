from django.urls import path
from blog.views import ArticleCreateView, BlogListView, BlogDetailView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create_article'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit_article'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete_article'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='article'),
]
