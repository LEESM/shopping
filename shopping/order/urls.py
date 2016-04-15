from django.conf.urls import url, include
from order import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),
    url(r'^cart_update/', views.cart_update, name='cart_update'),
    url(r'^order_info/', views.order_info, name='order_info'),
]