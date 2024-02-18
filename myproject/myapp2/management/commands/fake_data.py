from django.core.management.base import BaseCommand
from myapp2.models import Product, Order, User
class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        # count = kwargs.get('count')
        # for i in range(1, count + 1):
        #     product = Product(name=f'Product{i}',
        #                       description=f'Product for cocking{i}',
        #                       price=i+2.2,
        #                       quantity=i+1)
        #     product.save()

        pk1 = kwargs['pk']
        selected_products = Product.objects.all()
        total_amount = sum(Product.objects.get(pk=product.pk).price for product in selected_products)
        print(str(total_amount))
        user = User.objects.filter(pk=pk1).first()
        order = Order(total_price=total_amount, customer=user)
        order.products.set(selected_products)
        # order.save()
        # self.stdout.write(f'{user}')
