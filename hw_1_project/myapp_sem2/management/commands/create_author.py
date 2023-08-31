import datetime

from django.core.management.base import BaseCommand
from myapp_sem2.models import Author
import datetime


class Command(BaseCommand):
    help = 'Create author'

    def handle(self, *args, **kwargs):
        for i in range(10):
            author = Author(name=f'name{i}', surname=f'surname{i}', email=f'email{i}@mail.ru',
                            biography='bla, bla, bla', birthday=datetime.date.today())
            author.save()
        self.stdout.write(f'10 authors created')
