from django.db import models
from django.utils.timezone import now


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата изменения')
    manufactured_at = models.DateField(default=now, verbose_name='Дата производства')

    def __str__(self):
        return f'продукт'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'категория'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
