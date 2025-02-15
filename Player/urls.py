from django.urls import path, include
from .views import PlayerProfileApi
from rest_framework import routers

router = routers.DefaultRouter()

router.register('create_profile', PlayerProfileApi, basename='create_profile')

urlpatterns = [
    path('', include(router.urls)),
]