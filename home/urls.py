from django.urls import path
from .views import *

urlpatterns = [
    path('', views.home_page, name="home"),
    path('contact/', views.contact, name="contact"),
    path('menu/', views.menu, name="menu"),
    path('about/', views.about, name="about"),
]