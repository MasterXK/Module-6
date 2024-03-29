from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        categories_to_add = [
            {'name': 'категория1', 'description': 'описание1'},
            {'name': 'категория2', 'description': 'описание2'},
            {'name': 'категория3', 'description': 'описание3'},
        ]

        products_to_add = [
            {'name': 'продукт1', 'price': '1', 'category': Category.objects.get(name='категория1'), 'description': 'описание1'},
            {'name': 'продукт2', 'price': '2', 'category': Category.objects.get(name='категория1'), 'description': 'описание2'},
            {'name': 'продукт3', 'price': '3', 'category': Category.objects.get(name='категория2'), 'description': 'описание3'},
            {'name': 'продукт4', 'price': '4', 'category': Category.objects.get(name='категория3'), 'description': 'описание4'},
        ]

        categories_to_create = []
        for category in categories_to_add:
            categories_to_create.append(Category(**category))

        Category.objects.bulk_create(categories_to_create)

        products_to_create = []
        for product in products_to_add:
            products_to_create.append(Product(**product))

        Product.objects.bulk_create(products_to_create)


