from django.shortcuts import render, redirect
from .forms import TournamentForm
from django.http import Http404
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from . serializers import TournamentApiSerializer, CreateTournamentSerializer, UpdateTournamentSerializer
from .models import Tournament, Player, SignUp

class TournamentApi(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Tournament.objects.all()
    serializer_class = TournamentApiSerializer
    html_path = 'tournament/tournament.html'
    detail_html_path = 'tournament/tournament_detail.html'
    create_html_path = "tournament/tournament_create.html"
    
    def list(self, request, *args, **kwargs):
        tournaments = Tournament.objects.all()
        form = TournamentForm()
        return render(request, self.html_path, {'tournaments': tournaments, 'form': form})
    
    def create(self, request, *args, **kwargs):
        if request.method == "POST":
            serializer = TournamentApiSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save() 
                return redirect('tournament-list')
        else:
            serializer = TournamentApiSerializer()

        return render(request, 'tournament/tournament_create.html', {'serializer': serializer})
    
    def update(self, request, *args, **kwargs):
        tournament = self.get_object()
        if request.method == "POST":
            serializer = TournamentApiSerializer(tournament, data=request.POST, partial=True)
            if serializer.is_valid():
                serializer.save()
                return redirect('tournament-list')
        else:
            serializer = TournamentApiSerializer(tournament)
            
        return render(request, 'tournament/tournament_update.html', {'serializer': serializer})
    
    def retrieve(self, request, *args, **kwargs):
        try:
            tournament = self.get_object()
        except Http404:
            return render(request, self.detail_html_path, {'tournament': None})
        return render(request, self.detail_html_path, {'tournament': tournament})
    
    def destroy(self, request, *args, **kwargs):
        tournament = self.get_object()
        tournament.delete()
        return redirect('tournament-list')
    
    def check_form(self, form):
        if form.is_valid():
            form.save()
            return redirect('tournament-list')
