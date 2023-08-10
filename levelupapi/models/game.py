from django.db import models


class Game(models.Model):
    game = models.CharField(max_length=50)
    type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name='game')
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)