from django.db import models


class EventLog(models.Model):
    attendee = models.ForeignKey('Gamer', on_delete=models.CASCADE,related_name='eventAttending')
    attendedEvent = models.ForeignKey('Event', on_delete=models.CASCADE,related_name='log')
    gamePlayed = models.ForeignKey('Game', on_delete=models.CASCADE,related_name='gameEvents')
    
   