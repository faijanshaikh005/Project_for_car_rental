from django.contrib import admin
from django.urls import path, include
from .views import loginUser,logoutUser,homepage
from . import views

urlpatterns = [
    # path("", views.index, name='home'),
    path("loginUser/", views.loginUser, name='loginUser'),
    path("looutUser/", views.logoutUser, name='logoutUser'),
    path("admin_homepage/", views.homepage, name='logoutUser'),
 ]