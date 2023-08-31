from django.core.management.base import BaseCommand
from myapp_sem2.models import Author, Post
from random import randint


class Command(BaseCommand):
    help = 'Create posts'

    def handle(self, *args, **kwargs):
        for author in Author.objects.all():
            for i in range(randint(1, 5)):
                post = Post(
                    title=f'head_{i}',
                    content=f'bla-bla-bla {i}',
                    author=author,
                    category=f'category_{i}',
                    public=randint(0, 1),
                )
                post.save()
        self.stdout.write('articles created')
