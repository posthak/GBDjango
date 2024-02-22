# from django.core.management.base import BaseCommand
# from e_shop.models import Product, Order, User
# class Command(BaseCommand):
#     help = "Generate fake Product, Order."
#
#     def add_arguments(self, parser):
#         parser.add_argument('count', type=int, help='count')
    # def handle(self, *args, **kwargs):
    #     product_list = [
    #         {'name': 'Смарт часы', 'description': 'Смарт часы',
    #          'price': 500.00, 'quantity': 20},
    #         {'name': 'Телефон Самсунг', 'description': 'Телефон Самсунг',
    #          'price': 1000, 'quantity': 10},
    #         {'name': 'Наушники Аппл', 'description': 'Наушники Аппл',
    #          'price': 100, 'quantity': 50}
    #     ]
    #     product_for_create = []
    #     for product_item in product_list:
    #         product_for_create.append(
    #             Product(**product_item)
    #         )
    #     Product.objects.bulk_create(product_for_create)
    #
    #     order_list = [
    #         {'total_price': 1600, 'customer': User.objects.get(pk=1), 'product': Product.objects.get(pk=1)},
    #         {'total_price': 1600, 'customer': User.objects.get(pk=1),  'product': Product.objects.get(pk=2)},
    #         {'total_price': 1600, 'customer': User.objects.get(pk=1), 'product': Product.objects.get(pk=3)},
    #         {'total_price': 1500, 'customer': User.objects.get(pk=2),  'product': Product.objects.get(pk=1)},
    #         {'total_price': 1500, 'customer': User.objects.get(pk=2),  'product': Product.objects.get(pk=2)},
    #         {'total_price': 500, 'customer': User.objects.get(pk=3),  'product': Product.objects.get(pk=1)},
    #     ]
    #     order_for_create = []
    #     for order in order_list:
    #         order_for_create.append(
    #             Order(**order)
    #         )
    #     Order.objects.bulk_create(order_for_create)

    # def handle(self, *args, **kwargs):
    #     count = kwargs.get('count')
    #     for i in range(1, count + 1):
    #         user = User(name=f'User{i}', email=f'user{i}@django.com', mob_number=f'022022897{i}', address=f'Address {i}')
    #         user.save()
    #         for j in range(1, count + 1):
    #             product = Product(name=f'Смарт часы {j+i}', description=f'Смарт часы {i+j}', price=i+j*100.02, quantity=i+j+5,
    #                               date_created='2023-12-17')
    #             product.save()
    #             order = Order(total_price=i+j*100.02, customer=user, product=product, order_date='2024-02-15')
    #             order.save()

from django.core.management.base import BaseCommand
from faker_commerce import Provider
from e_shop.models import User, Product, Order
from faker import Faker
import random
from decimal import Decimal
import faker_commerce

class Command(BaseCommand):
    help = 'Create fake data'

    def handle(self, *args, **options):
        fake = Faker()

        users = [User.objects.create(name=fake.name(), email=fake.email(),
                                     mob_number=fake.msisdn(), address=fake.address()) for _ in range(5)]
        fake.add_provider(faker_commerce.Provider)
        products = [Product.objects.create(name=fake.ecommerce_name(), description=fake.sentence(),
                                           price=Decimal(random.uniform(10, 100)), quantity=(random.randint(1, 20)),
                                           date_created='2023-12-10') for _ in range(10)]

        for _ in range(2):
            user = random.choice(users)
            order_products = random.sample(products, random.randint(1, 5))
            total_price = sum(product.price for product in order_products)
            order = Order.objects.create(user=user, total_price=total_price, order_date='2024-02-21')
            order.products.set(order_products)

        self.stdout.write(self.style.SUCCESS('Fake data created!'))
