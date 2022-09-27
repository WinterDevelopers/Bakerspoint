from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('product', views.productPageData, name='project-data')
]