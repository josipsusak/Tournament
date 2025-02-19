from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TournamentApi

router = DefaultRouter()
router.register('tournaments', TournamentApi, basename='tournament')

tournament_create_view = TournamentApi.as_view({'get': 'create', 'post': 'create'})
tournament_update_view = TournamentApi.as_view({'get': 'update', 'post': 'update'})
tournament_delete_view = TournamentApi.as_view({'post': 'destroy'})  

urlpatterns = [
    path('tournaments/create/', tournament_create_view, name='tournament-create'),
    path('tournaments/<int:pk>/update/', tournament_update_view, name='tournament-update'),
    path('tournaments/<int:pk>/delete/', tournament_delete_view, name='tournament-delete'), 
    path('', include(router.urls)),  
]
