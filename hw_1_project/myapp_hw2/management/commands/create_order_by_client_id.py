from django.core.management.base import BaseCommand
from myapp_hw2.models import Order, Client, Product

class Command(BaseCommand):
    help = 'Create order by client id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('title', type=str, help='Product title')
        parser.add_argument('description', type=str, help='Product description')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        title = kwargs.get('title')
        product_1 = Product.objects.filter(title=title).first()
        # уменьшаем количество товара в базе
        product_1.count -= 1
        product_1.save()
        description = kwargs.get('description')
        product_2 = Product.objects.filter(description=description).first()
        product_2.count -= 1
        product_2.save()
        order = Order(
            client=client,
            price=product_1.price + product_2.price,
        )
        order.save()
        order.product.set({product_1, product_2})
        self.stdout.write(f'{order}')
