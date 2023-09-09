from django.shortcuts import render
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
