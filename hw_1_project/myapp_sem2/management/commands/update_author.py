from django.core.management.base import BaseCommand
from myapp_sem2.models import Author


class Command(BaseCommand):
    help = 'Update author name and surname by id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('name', type=str, help='Author name')
        parser.add_argument('surname', type=str, help='Author surname')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        surname = kwargs.get('surname')
        author = Author.objects.filter(pk=pk).first()
        author.name = name
        author.surname = surname
        author.save()
        self.stdout.write(f'{author}')
