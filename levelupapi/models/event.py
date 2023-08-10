from django.db import models



class Event(models.Model):

    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name='Gamers')