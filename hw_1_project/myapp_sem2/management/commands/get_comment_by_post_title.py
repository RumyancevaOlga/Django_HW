from django.core.management.base import BaseCommand
from myapp_sem2.models import Comment


class Command(BaseCommand):
    help = 'Get comments by post title.'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Post title')

    def handle(self, *args, **kwargs):
        title = kwargs.get('title')
        comments = Comment.objects.filter(post__title=title)
        intro = f'All comments\n'
        text = '\n'.join(comment.get_summary() for comment in comments)
        self.stdout.write(f'{intro}{text}')
