from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coin/', views.coin, name='coin'),
    path('cube/', views.cube, name='cube'),
    path('rand100/', views.rand100, name='rand100'),
    path('posts/<int:author_id>', views.get_posts, name='get_posts'),
    path('post/<int:post_id>', views.get_post, name='get_post'),
]
