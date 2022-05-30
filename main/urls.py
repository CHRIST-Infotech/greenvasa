from django.urls import path

from . import views

app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products_details/<int:id>', views.product_details),
]