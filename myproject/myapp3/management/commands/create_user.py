from django.core.management.base import BaseCommand
from myapp3.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        # user = User(name='Oleg', email='oleg@example.com', mob_number='02202221122',
        #             address='Lenina 12')
        # user = User(name='Ivan', email='Ivan@example.com', mob_number='02202221132',
        #             address='Pushkina 2')
        user = User(name='Petr', email='Petr@example.com', mob_number='0220228978',
                    address='Tverskaya 200')
        # user = User(name='Nikolai', email='Nikolai@example.com', mob_number='024441122',
        #             address='Gogolya 62')
        user.save()
        self.stdout.write(f'{user}')
