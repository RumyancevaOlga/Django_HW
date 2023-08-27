from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse(f'<h1>Главная страница</h1>' \
                        f'<a href="http://127.0.0.1:8000/about"><b>О себе</b></a>' \
                        f'<p>Это мой <i>первый</i> проект на Джанго!</p>' \
                        f'<hr>' \
                        f'<p>Все права защищены &copy</p>')


def about(request):
    logger.info('About page accessed')
    return HttpResponse(f'<h1>О себе</h1>' \
                        f'<p>Меня зовут Ольга. Мне 33 года. Я учусь в <b>GeekBrains</b>.<br>' \
                        f'Надеюсь стать классным специалистом в разработке на <i>python</i></p>' \
                        f'<hr>' \
                        f'<p>Все права защищены &copy</p>')
