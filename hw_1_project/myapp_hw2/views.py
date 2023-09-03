from django.shortcuts import render
from .models import Order, Client
import datetime


# Доработаем задачу 8 из прошлого семинара про клиентов,
# товары и заказы.
# Создайте шаблон для вывода всех заказов клиента и
# списком товаров внутри каждого заказа.
# Подготовьте необходимый маршрут и представление.

def client_orders(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client)
    context = {'client': client, 'orders': orders}
    return render(request, 'myapp_hw2/client_orders.html', context)


# Продолжаем работать с товарами и заказами.
# Создайте шаблон, который выводит список заказанных
# клиентом товаров из всех его заказов с сортировкой по
# времени:
# ○ за последние 7 дней (неделю)
# ○ за последние 30 дней (месяц)
# ○ за последние 365 дней (год)
# *Товары в списке не должны повторятся.
def client_products(request, client_id, date):
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client)
    if date == 'week':
        date = datetime.datetime.now() - datetime.timedelta(weeks=1)
    elif date == 'year':
        date = datetime.datetime.now() - datetime.timedelta(weeks=52)
    else:
        date = datetime.datetime.now() - datetime.timedelta(days=30)
    context = {'client': client, 'orders': orders, 'date': date}
    return render(request, 'myapp_hw2/client_products.html', context)
