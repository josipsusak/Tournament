from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from .serializers import LoginSerializer, SignupSerializer


class LoginView(View):
    template_name = 'Player/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.POST, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return redirect('tournament-list')
        return render(request, self.template_name, {'errors': serializer.errors})

class SignupView(View):
    template_name = 'Player/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('Player:login')
        return render(request, self.template_name, {'errors': serializer.errors})

class HomeView(View):
    template_name = 'Player/home.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('Player:login')
        return render(request, self.template_name)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('Player:login')


        