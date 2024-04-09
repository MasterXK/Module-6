from django.urls import path
from blog.views import ArticleCreateView, BlogListView, BlogDetailView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create_article'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='article'),
]
