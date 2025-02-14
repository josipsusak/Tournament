from django.urls import path, include
from .views import TournamentApi
from rest_framework import routers

router = routers.DefaultRouter()

router.register('tournaments', TournamentApi, basename='tournament')

urlpatterns = [
    path('', include(router.urls))
]