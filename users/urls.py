from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('read', views.read, name='user_read'),
    path('create', views.create, name='user_create'),
    path('update', views.update, name='user_update'),
    path('delete', views.delete, name='user_delete'),
]