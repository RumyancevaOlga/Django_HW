# *Допишите несколько функций CRUD для работы с
# моделями по желанию. Что по вашему мнению актуально в
# такой базе данных.

from django.core.management.base import BaseCommand
from myapp_hw2.models import Client


class Command(BaseCommand):
    help = 'Update telephone by client id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('telephone', type=int, help='New telephone')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        telephone = kwargs.get('telephone')
        client = Client.objects.filter(pk=pk).first()
        client.telephone = telephone
        client.save()
        self.stdout.write(f'{client}')