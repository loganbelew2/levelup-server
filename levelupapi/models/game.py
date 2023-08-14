from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=50)
    type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name='games')
    maker = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    skill_level = models.IntegerField(default=0)
    number_of_players = models.IntegerField(default=0)