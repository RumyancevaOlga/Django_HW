from django.core.management.base import BaseCommand
from myapp_hw2.models import Client


class Command(BaseCommand):
    help = 'Create client.'

    def handle(self, *args, **kwargs):
        # client = Client(name='Ivan', email='ivan@example.com', telephone=11111, address='TmuTarakanya')
        # client = Client(name='Bruce', email='bruce@example.com', telephone=67895, address='Gotham')
        client = Client(name='Johnny', email='johnny@example.com', telephone=12345, address='Night city')
        # client = Client(name='Elrond', email='elrond@example.com', telephone=12345, address='Rivendell')
        client.save()
        self.stdout.write(f'{client}')
