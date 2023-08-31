# Создайте функции для работы с базой данных:
# ○ Поиск всех статей автора по его имени
# ○ Поиск всех комментариев автора по его имени
# ○ Поиск всех комментариев по названию статьи
# Каждая из трёх функций должна иметь возможность
# сортировки и ограничение выборки по количеству.

from django.core.management.base import BaseCommand
from myapp_sem2.models import Post


class Command(BaseCommand):
    help = 'Get post by author name.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Author name')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        posts = Post.objects.filter(author__name=name)
        intro = f'All posts\n'
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')
