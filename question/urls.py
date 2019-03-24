from django.conf.urls import url
from django.urls import path
from question import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
]
