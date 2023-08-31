from django.core.management.base import BaseCommand
from myapp_hw2.models import Order

class Command(BaseCommand):
    help = 'Get order by client id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        orders = Order.objects.filter(client__pk=pk)
        intro = f'All orders\n'
        text = '\n'.join(order.get_summary() for order in orders)
        self.stdout.write(f'{intro}{text}')
