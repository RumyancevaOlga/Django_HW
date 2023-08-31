from django.core.management.base import BaseCommand
from myapp_hw2.models import Product


class Command(BaseCommand):
    help = 'Create product.'

    def handle(self, *args, **kwargs):
        # product = Product(title='milk', description="cow's milk", price=55.7, count=100)
        # product = Product(title='chocolate', description="milk chocolate", price=110.5, count=50)
        product = Product(title='eggs', description="chicken eggs", price=74.3, count=55)
        # product = Product(title='bread', description="wheat bread", price=35.4, count=150)
        product.save()
        self.stdout.write(f'{product}')
