from django.db import models



class Event(models.Model):
    title = models.CharField(max_length=50)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='events')
    date = models.DateField( auto_now = False, auto_now_add = False)
    location = models.CharField(max_length=50)
    attendees = models.ManyToManyField('Gamer', through= 'EventLog')
    gameId = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='gameEvents')