from django.contrib import admin
from django.urls import path, include
from accounts import views 


urlpatterns = [
    path('signup', views.signup, name='signup1'),
    path('login', views.login, name='login1'),
]