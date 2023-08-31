from django.core.management.base import BaseCommand
from myapp_sem2.models import Comment


class Command(BaseCommand):
    help = 'Get comments by author name.'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Author name')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        comments = Comment.objects.filter(author__name=name)
        intro = f'All comments\n'
        text = '\n'.join(comment.get_summary() for comment in comments)
        self.stdout.write(f'{intro}{text}')
