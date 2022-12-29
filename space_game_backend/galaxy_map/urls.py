from django.contrib import admin
from django.urls import path, include
from .views import SystemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('systems', SystemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
