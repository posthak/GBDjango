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

        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        order = Order(total_price=10.2, customer=user)
        order.save()
        self.stdout.write(f'{user}')
