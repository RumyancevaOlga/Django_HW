from django.core.management.base import BaseCommand
from myapp_sem2.models import Author, Post, Comment
from random import randint


class Command(BaseCommand):
    help = 'Create comments'

    def handle(self, *args, **kwargs):
        for author in Author.objects.all():
            for post in Post.objects.all():
                for i in range(randint(1, 2)):
                    comment = Comment(
                        author=author,
                        post=post,
                        comment=f'Very impotent comment_{i}',
                    )
                    comment.save()
        self.stdout.write('comments created')
