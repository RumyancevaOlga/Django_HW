# Создай четыре функции для реализации CRUD в модели
# Django Article (статья).

from django.core.management.base import BaseCommand
from myapp_sem2.models import Post


class Command(BaseCommand):
    help = 'Get post by author id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')
