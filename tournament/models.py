from django.db import models
from Player.models import Player

class Tournament(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('ongoing', 'Ongoing'),
        ('finished', 'Finished'),
    )

    name = models.CharField(max_length=100, unique=True)
    game = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    num_of_players = models.IntegerField()
    creator = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='created_tournaments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TournamentRegistration(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='registrations')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('player', 'tournament')

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name} - {self.tournament.name}"
    