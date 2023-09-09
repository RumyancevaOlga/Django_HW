from django.db import models


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


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    public_date = models.DateTimeField(auto_now=True)
    change_date = models.DateTimeField(auto_now=True)
