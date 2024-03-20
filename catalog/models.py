from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    creation_date = models.DateField(verbose_name='Дата создания')
    last_change_date = models.DateField(verbose_name='Дата изменения')

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
