from django.core.management.base import BaseCommand
from myapp_hw2.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Create orders.'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for client in Client.objects.all():
            order = Order(
                client=client,
                price=sum(product.price for product in products),
                )
            order.save()
            order.product.set(products)
            self.stdout.write(f'{order}')
