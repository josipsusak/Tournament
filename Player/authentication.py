from django.contrib.auth.backends import BaseBackend
from .models import Player

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            player = Player.objects.get(email=email)
            if player.check_password(password):
                return player
        except Player.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Player.objects.get(pk=user_id)
        except Player.DoesNotExist:
            return None