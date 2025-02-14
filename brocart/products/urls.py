from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('list_product',views.list_product,name='list_product'),
    path('detail_product',views.detail_product,name='detail_product')

]
