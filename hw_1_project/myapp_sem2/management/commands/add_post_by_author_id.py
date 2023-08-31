from django.core.management.base import BaseCommand
from myapp_sem2.models import Post, Author


class Command(BaseCommand):
    help = 'Add post by author id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('title', type=str, help='Post title')
        parser.add_argument('category', type=str, help='Post category')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author= Author.objects.filter(pk=pk).first()
        title = kwargs.get('title')
        category = kwargs.get('category')
        post = Post(
            title=title,
            content='new bla-bla',
            category=category,
            author=author,
            public=True,
        )
        post.save()
        self.stdout.write(f'{post}')
