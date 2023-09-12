from django.contrib import admin
from .models import Product, Order, Client


# Настройте под свои нужды вывод информации о клиентах, товарах и заказах на страницах вывода информации
# об объекте и вывода списка объектов.

@admin.action(description='Сбросить количество товара')
def reset_count(modeladmin, request, queryset):
    queryset.update(count=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'address', 'telephone']
    ordering = ['name', 'address']
    search_fields = ['telephone']
    search_help_text = 'Поиск по номеру телефона'
    fields = ['name', 'email', 'address', 'telephone', 'registrations_date']
    readonly_fields = ['registrations_date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'count']
    ordering = ['title', 'price']
    actions = [reset_count]
    readonly_fields = ['change_date', 'photo']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Описание товара и его фото',
                'fields': ['description', 'photo'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            },
        ),
        (
            'Дата последнего изменения',
            {
                'fields': ['change_date'],
            },
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'price', 'registrations_date']
    ordering = ['client', 'registrations_date']
    fields = ['client', 'price', 'product', 'registrations_date']
    readonly_fields = ['client', 'price', 'product', 'registrations_date']


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
