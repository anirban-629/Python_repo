# import imp
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('',views.base,name='Base'),
    path('home',views.home,name='Home'),
    path('about',views.about,name='About'),
    path('contact',views.contact,name='Contact')
]