from django.contrib import admin
from django.urls import path

from . import views

app_name = 'store'
urlpatterns = [
    path('<slug:name>/', views.productPage, name='product_page' ),
    path('products/<slug:slug>', views.productItem, name = 'product_item')
]