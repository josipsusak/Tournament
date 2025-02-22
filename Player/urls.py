from django.urls import path
from .views import LoginView, SignupView, HomeView, LogoutView

app_name = 'Player'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout')
]