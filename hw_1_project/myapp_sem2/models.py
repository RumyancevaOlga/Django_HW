from django.db import models
from datetime import datetime
from random import randint
from collections import deque


class Coin(models.Model):
    result = models.BooleanField()
    kick_time = models.DateTimeField(default=datetime.now())

    # @staticmethod
    # def statistics(n: int):
    #     reshka = 0
    #     orel = 0
    #     for _ in range(n):
    #         kick = Coin(result=randint(0, 1))
    #         if kick.result:
    #             reshka += 1
    #         else:
    #             orel += 1
    #     result_dict = {
    #         'орёл': orel,
    #         'решка': reshka,
    #     }
    #     return result_dict

    @staticmethod
    def statistics(n: int):
        coins = deque(Coin.objects.all(), maxlen=n)
        result = {
            'heads': 0,
            'tails': 0
        }
        for coin in coins:
            if coin.flip:
                result['heads'] += 1
            else:
                result['tails'] += 1
        return result


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    public_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count = models.IntegerField(default=0)
    public = models.BooleanField()

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words)}'


# Создайте модель Комментарий.
# Авторы могут добавлять комментарии к своим и чужим
# статьям. Т.е. у комментария может быть один автор.
# И комментарий относится к одной статье. У модели должны
# быть следующие поля
# ○ автор
# ○ статья
# ○ комментарий
# ○ дата создания
# ○ дата изменения
class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    public_date = models.DateTimeField(auto_now=True)
    change_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment is {self.comment}'

    def get_summary(self):
        words = self.comment.split()
        return f'{" ".join(words)}'
