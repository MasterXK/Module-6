from django.contrib import admin
from blog.models import BlogArticle


@admin.register(BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views')
    list_filter = ('title',)
    search_fields = ('title', 'text')
