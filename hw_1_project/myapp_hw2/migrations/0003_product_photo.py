# Generated by Django 4.2.4 on 2023-09-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp_hw2', '0002_remove_order_product_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
