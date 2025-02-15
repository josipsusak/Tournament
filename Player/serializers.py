from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.EmailField()
    

class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'