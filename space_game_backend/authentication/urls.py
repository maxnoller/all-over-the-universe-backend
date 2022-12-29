from django.contrib import admin
from django.urls import path, include

from .views import set_csrf_token, login_view

urlpatterns = [
  path('set-csrf/', set_csrf_token, name='Set-CSRF'),
  path('login/', login_view, name='Login'),
]
