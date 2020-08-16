from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.shownotif, name='notifications'),
    path('', views.sendnotif, name='sendnotif')
]
