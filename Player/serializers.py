from rest_framework import serializers
from .models import Player
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

class PlayerSerializer(serializers.Serializer):
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.EmailField()
    

class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError("Pogrešan email ili šifra.")
        else:
            raise serializers.ValidationError("Morate unijeti email i šifru.")

        data['user'] = user
        return data

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Player.objects.create(**validated_data)