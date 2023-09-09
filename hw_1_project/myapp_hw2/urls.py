from django.urls import path
from . import views

urlpatterns = [
    path('order/<int:client_id>/', views.client_orders, name='order'),
    path('products/<int:client_id>/<str:date>', views.client_products, name='order'),
]
