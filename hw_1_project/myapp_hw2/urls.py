from django.urls import path
from . import views

urlpatterns = [
    path('change_product/<int:product_id>/', views.product_form, name='change_product'),
    path('upload_image_to_product/<int:product_id>/', views.upload_image_to_product, name='upload_image_to_product'),
    path('order/<int:client_id>/', views.client_orders, name='order'),
    path('products/<int:client_id>/<str:date>', views.client_products, name='order'),
]
