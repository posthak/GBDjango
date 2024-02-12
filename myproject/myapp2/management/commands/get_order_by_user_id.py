from django.core.management.base import BaseCommand
from myapp2.models import Order, User

class Command(BaseCommand):
    help = "Get order by user id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(customer__pk=pk)
        order = '\n'.join(str(ord.total_price)+' | '+str(ord.date_ordered) + ' | ' +str(ord.customer.name)
                          for ord in order)
        self.stdout.write(f'{order}')
