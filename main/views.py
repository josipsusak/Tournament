from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from . serializers import TournamentSerializer, CreateTournamentSerializer
from .models import Tournament, Player, SignUp

class TournamentApi(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    
    
    def list(self, request, *args, **kwargs):
        tournaments = Tournament.objects.all()
        return render(request, 'tournament.html', {'tournaments': tournaments})
    
    def create(self, request, *args, **kwargs):
        serializer = CreateTournamentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        tournaments = Tournament.objects.all()
        return render(request, 'tournament.html', {'tournaments': tournaments})
    
    def destroy(self, request, *args, **kwargs):
        tournament = self.get_object()
        tournament.delete()
        tournaments = Tournament.objects.all()
        return render(request, 'tournament.html', {'tournaments': tournaments})