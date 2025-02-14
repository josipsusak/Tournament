from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, default=None)
    game = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    num_of_players = models.IntegerField()
    

    def __str__(self):
        return self.name

class Player(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname

class SignUp(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    time_of_signup = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.tournament.name + ' - ' + self.player.firstname + ' ' + self.player.lastname
    