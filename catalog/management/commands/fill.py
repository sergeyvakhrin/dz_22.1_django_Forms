import json
from datetime import datetime
from pathlib import Path

from django.core.management import BaseCommand

from catalog.models import Product, Category, Contact


class Command(BaseCommand):

    def load_data(self) -> list[dict]:
        """ Метод для загрузки данных из json """
        ROOT_PATH = Path(__file__).parent.parent.parent.parent
        DATA_PATH = ROOT_PATH.joinpath('catalog.json')
        with open(DATA_PATH, 'rt', encoding="UTF-8") as file:
            catalog = json.load(file)
        return catalog

    def get_category(self, catalog) -> list:
        """ Метод для получения списка экземпляров Класса Category для заполнения базы данных """
        category_for_create = []
        for category in catalog:
            data = category['fields']
            if category['model'] == 'catalog.category':
                category_for_create.append(Category(
                    category_name=data['category_name'],
                    category_description=data.get('category_description', None),
                    pk=category['pk']
                ))
        return category_for_create

    def get_product(self, catalog) -> list:
        """ Метод для получения списка экземпляров Класса Product для заполнения базы данных """
        product_for_create = []
        for product in catalog:
            data = product['fields']
            if product['model'] == 'catalog.product':
                valid_cat = Category.objects.get(pk=data.get('category')) if data['category'] else None
                product_for_create.append(Product(
                    pk=product['pk'],
                    product_name=data['product_name'],
                    product_description=data['product_description'],
                    product_image=data['product_image'],
                    category=valid_cat,
                    price=data['price'],
                    created_at=data.get('created_at', datetime.now()),
                    updated_at=data.get('created_up',datetime.now()),
                ))
        return product_for_create

    def get_contact(self, catalog):
        """ Метод для получения списка экземпляров Класса Catalog для заполнения базы данных """
        catalog_for_create = []
        for category in catalog:
            data = category['fields']
            if category['model'] == 'catalog.contact':
                catalog_for_create.append(Contact(
                    name=data['name'],
                    phone=data.get('phone', None),
                    message=data.get('message', None),
                    pk=category['pk']
                ))
        return catalog_for_create

    def handle(self, *args, **options) -> None:
        """ Метод автоматически срабатывает при обращении к коменде fill """

        print("Загрузка данных")
        catalog = self.load_data()

        print("Очистка Базы данных")
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contact.objects.all().delete()

        print("Создание Категорий")
        category_for_create = self.get_category(catalog)
        Category.objects.bulk_create(category_for_create)

        print("Создание Продуктов")
        product_for_create = self.get_product(catalog)
        Product.objects.bulk_create(product_for_create)

        print("Создание Контактов")
        catalog_for_create = self.get_contact(catalog)
        Contact.objects.bulk_create(catalog_for_create)


