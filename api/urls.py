from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Elevators', ElevatorViewSet)
router.register(r'Request', RequestViewSet)
urlpatterns = [
    path('', include(router.urls))
]

