from django.contrib import admin
from django.urls import path,include
from milo_main import views
urlpatterns = [
    path('',views.home,name='milo_home')
]
