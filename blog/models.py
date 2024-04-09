from django.db import models


class BlogArticle(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    text = models.TextField(verbose_name='Cодержимое')
    preview = models.ImageField(verbose_name='Изображение')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликованно')
    views = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'Статья {self.title} от {self.created_at}; {self.slug}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
