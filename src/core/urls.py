from django.contrib import admin
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clients, name='clients'),
    path('productos/', views.products, name='products')
]
