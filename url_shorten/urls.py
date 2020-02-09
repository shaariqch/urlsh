from django.contrib import admin
from django.urls import path, include
from .views import home, redirect_to_site
urlpatterns = [
    path('', home),
    path('<str:encoded_url>/', redirect_to_site)
]