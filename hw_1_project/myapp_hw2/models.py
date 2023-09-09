# Создайте три модели Django: клиент, товар и заказ. Клиент
# может иметь несколько заказов. Заказ может содержать
# несколько товаров. Товар может входить в несколько
# заказов.
from django.db import models


# Поля модели "Клиент":
# ○ имя клиента
# ○ электронная почта клиента
# ○ номер телефона клиента
# ○ адрес клиента
# ○ дата регистрации клиента

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.IntegerField()
    address = models.CharField(max_length=200)
    registrations_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


# Поля модели "Товар":
# ○ название товара
# ○ описание товара
# ○ цена товара
# ○ количество товара
# ○ дата добавления товара

class Product(models.Model):
    # Измените модель продукта, добавьте поле для хранения фотографии продукта.
    # Создайте форму, которая позволит сохранять фото.
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    change_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(null=True, default=None)

    def __str__(self):
        return f'title: {self.title}, price: {self.price}'


# Поля модели "Заказ":
# ○ связь с моделью "Клиент", указывает на клиента,
# сделавшего заказ
# ○ связь с моделью "Товар", указывает на товары,
# входящие в заказ
# ○ общая сумма заказа
# ○ дата оформления заказа

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    registrations_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Name: {self.client.name}, price: {self.price}'

    def get_summary(self):
        words = f'{self.price} {self.registrations_date}'
        return f'{"".join(words)}'
