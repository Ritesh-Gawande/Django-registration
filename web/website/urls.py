from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.register, name='register'),
]


