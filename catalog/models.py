from django.db import models

class Product(models.Model):
    def __str__(self):
        return f'продукт'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    def __str__(self):
        return f'категория'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
