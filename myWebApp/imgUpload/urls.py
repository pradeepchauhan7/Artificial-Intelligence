from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'imageprocess', views.imageprocess, name='imageprocess')
]