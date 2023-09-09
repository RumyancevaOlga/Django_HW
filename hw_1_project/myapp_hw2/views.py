from django.shortcuts import render
<<<<<<< HEAD
from .forms import ProductForm, ProductPhotoForm
from .models import Product


def product_form(request, product_id):
    message = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product(
                pk=product_id,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                count=form.cleaned_data['count']
            )
            product.save()
            message = 'Продукт изменен'
    else:
        form = ProductForm()
    return render(request, 'myapp_hw2/change_product.html',
                  {'form': form, 'message': message})


def upload_image_to_product(request, product_id):
    message = ''
    if request.method == 'POST':
        form = ProductPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
                pk=product_id,
                photo=form.cleaned_data['photo'],
                title=Product.objects.filter(pk=product_id).first().title,
                description=Product.objects.filter(pk=product_id).first().description,
                price=Product.objects.filter(pk=product_id).first().price,
                count=Product.objects.filter(pk=product_id).first().count
            )
            product.save()
            message = 'Изображение загружено'
    else:
        form = ProductPhotoForm()
    return render(request, 'myapp_hw2/upload_image.html', {'form': form, 'message': message,})
=======
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
>>>>>>> 3f27b301cc4ba52a21b966e14e6ccc65d7a3ec5e
