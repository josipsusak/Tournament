from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TournamentApi

router = DefaultRouter()
router.register('tournaments', TournamentApi, basename='tournament')

urlpatterns = [
    path('', include(router.urls)),
]
