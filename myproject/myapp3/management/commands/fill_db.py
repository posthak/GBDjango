from django.core.management.base import BaseCommand
from myapp3.models import Product, Order, User
class Command(BaseCommand):
    help = "Generate fake Product, Order."

    # def add_arguments(self, parser):
        # parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        product_list = [
            {'name': 'Смарт часы', 'description': 'Смарт часы',
             'price': 500.00, 'quantity': 20},
            {'name': 'Телефон Самсунг', 'description': 'Телефон Самсунг',
             'price': 1000, 'quantity': 10},
            {'name': 'Наушники Аппл', 'description': 'Наушники Аппл',
             'price': 100, 'quantity': 50}
        ]
        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )
        Product.objects.bulk_create(product_for_create)

        order_list = [
            {'total_price': 1600, 'customer': User.objects.get(pk=1), 'product': Product.objects.get(pk=1)},
            {'total_price': 1600, 'customer': User.objects.get(pk=1),  'product': Product.objects.get(pk=2)},
            {'total_price': 1600, 'customer': User.objects.get(pk=1), 'product': Product.objects.get(pk=3)},
            {'total_price': 1500, 'customer': User.objects.get(pk=2),  'product': Product.objects.get(pk=1)},
            {'total_price': 1500, 'customer': User.objects.get(pk=2),  'product': Product.objects.get(pk=2)},
            {'total_price': 500, 'customer': User.objects.get(pk=3),  'product': Product.objects.get(pk=1)},
        ]
        order_for_create = []
        for order in order_list:
            order_for_create.append(
                Order(**order)
            )
        Order.objects.bulk_create(order_for_create)
