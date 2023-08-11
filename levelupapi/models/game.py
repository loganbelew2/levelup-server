from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=50)
    type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name='games')
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)