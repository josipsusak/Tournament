from django.db import models

class Player(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname
