from django.contrib import admin

from .models import Tournament, Player, SignUp

admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(SignUp)
