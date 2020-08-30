from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('ask',views.askrisp,name="query"),
    path('temp',views.temp,name="temp"),
]
