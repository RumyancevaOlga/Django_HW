from django.urls import path
from . import views

urlpatterns = [
    path('change_product/<int:product_id>/', views.product_form, name='change_product'),
    path('upload_image_to_product/<int:product_id>/', views.upload_image_to_product, name='upload_image_to_product')
]
