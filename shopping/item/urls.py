from django.conf.urls import url, include
from item import views

urlpatterns = [
    url(r'^detail/', views.detail, name='detail'),
]