from rest_framework import serializers

from .models import Tournament

class TournamentApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'
        
class CreateTournamentSerializer(serializers.Serializer):
    name = serializers.CharField()
    game = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    num_of_players = serializers.IntegerField()
    
    def create(self, validated_data):
        return Tournament.objects.create(**validated_data)
    
    

class UpdateTournamentSerializer(serializers.Serializer):
    name = serializers.CharField(required=False)
    game = serializers.CharField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    num_of_players = serializers.IntegerField(required=False)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.game = validated_data.get('game', instance.game)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.num_of_players = validated_data.get('num_of_players', instance.num_of_players)
        instance.save()
        return instance