from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import Player
from .serializers import PlayerSerializer, PlayerProfileSerializer

class PlayerProfileApi(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Player.objects.all()
    serializer_class = PlayerProfileSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = PlayerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        player = Player.objects.get(id=serializer.data[id])
        return render(request, 'Player/create_player.html', {'player': player})
        