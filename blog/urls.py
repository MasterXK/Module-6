from django.urls import path
from blog.views import ArticleCreateView, BlogListView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create_article'),
    path('blog/', BlogListView.as_view(), name='blog_list')
]
