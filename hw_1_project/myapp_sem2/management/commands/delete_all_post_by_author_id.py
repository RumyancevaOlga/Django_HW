from django.core.management.base import BaseCommand
from myapp_sem2.models import Post, Author


class Command(BaseCommand):
    help = 'Delete all post by author id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        if author is not None:
            posts = Post.objects.filter(author=author)
            posts.delete()
        self.stdout.write(f'{author}')
