from django.shortcuts import render
from random import randint
from .models import Post, Comment


def index(request):
    return render(request, 'myapp_sem3/main.html')


def about(request):
    return render(request, 'myapp_sem3/about.html')


def coin(request):
    throw = randint(0, 1)
    throw = 'Решка' if throw else 'Орёл'
    context = {'result': throw}
    return render(request, 'myapp_sem3/games.html', context)


def cube(request):
    throw = randint(1, 6)
    context = {'result': throw}
    return render(request, 'myapp_sem3/games.html', context)


def rand100(request):
    throw = randint(0, 100)
    context = {'result': throw}
    return render(request, 'myapp_sem3/games.html', context)


def get_posts(request, author_id):
    posts = Post.objects.filter(author__pk=author_id)
    context = {'posts': posts}
    return render(request, 'myapp_sem3/posts.html', context)


# Измените шаблон для вывода заголовка и текста статьи, а
# также всех комментариев к статье с указанием текста
# комментария, автора комментария и даты обновления
# комментария в хронологическом порядке.
# Если комментарий изменялся, дополнительно напишите
# “изменено”.
# Не забывайте про представление с запросом в БД и
# маршруты. Проверьте, что они работают верно
def get_post(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    post.count += 1
    post.save()
    commenst = Comment.objects.filter(post__pk=post_id)
    context = {'post': post, 'comments': commenst}
    return render(request, 'myapp_sem3/post.html', context)
