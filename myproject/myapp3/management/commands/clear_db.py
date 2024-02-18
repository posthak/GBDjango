from django.core.management.base import BaseCommand
from myapp3.models import User, Product, Order

class Command(BaseCommand):
    help = "Delete user by id."

    # def add_arguments(self, parser):
        # parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        user = User.objects.all()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')

        product = Product.objects.all()
        if product is not None:
            product.delete()
        self.stdout.write(f'{product}')

        order = Order.objects.all()
        if order is not None:
            order.delete()
        self.stdout.write(f'{order}')
