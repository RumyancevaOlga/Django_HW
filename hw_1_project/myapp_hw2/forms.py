# Доработаем задачу про клиентов, заказы и товары из
# прошлого семинара.
# Создайте форму для редактирования товаров в базе
# данных.

from django import forms


class ProductForm(forms.Form):
    pk = forms.IntegerField(label='ID продукта')
    title = forms.CharField(label='Наименование товара', max_length=100)
    description = forms.CharField(label='Описание товара', widget=forms.Textarea)
    price = forms.DecimalField(label='Стоимость', max_digits=10, decimal_places=2)
    count = forms.IntegerField(label='Количество товара')


class ProductPhotoForm(forms.Form):
    photo = forms.ImageField()
