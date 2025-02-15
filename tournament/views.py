from django.shortcuts import render
from django.http import Http404
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import NotFound
from . serializers import TournamentApiSerializer, CreateTournamentSerializer, UpdateTournamentSerializer
from .models import Tournament, Player, SignUp

class TournamentApi(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Tournament.objects.all()
    serializer_class = TournamentApiSerializer
    html_path = 'tournament/tournament.html'
    detail_html_path = 'tournament/tournament_detail.html'
    
    def list(self, request, *args, **kwargs):
        tournaments = Tournament.objects.all()
        return render(request, self.html_path, {'tournaments': tournaments})
    
    def create(self, request, *args, **kwargs):
        serializer = CreateTournamentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        tournaments = Tournament.objects.all()
        return render(request, self.html_path, {'tournaments': tournaments})
    
    def update(self, request, *args, **kwargs):
        tournament = self.get_object()
        serializer = UpdateTournamentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(tournament, serializer.validated_data)
        tournaments = Tournament.objects.all()
        return render(request, self.html_path, {'tournaments': tournaments})
    
    def retrieve(self, request, *args, **kwargs):
        try:
            tournament = self.get_object()
        except Http404:
            return render(request, self.detail_html_path, {'tournament': None})
        return render(request, self.detail_html_path, {'tournament': tournament})
    
    def destroy(self, request, *args, **kwargs):
        tournament = self.get_object()
        tournament.delete()
        tournaments = Tournament.objects.all()
        return render(request, self.html_path, {'tournaments': tournaments})
