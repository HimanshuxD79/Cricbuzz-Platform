from django.db import models

# Create your models here.
class Players(models.Model):
    player_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=256,null=False,blank=False)
    matches_played = models.IntegerField()
    runs = models.IntegerField()
    average = models.FloatField(null=True, blank=True, default=None)
    strike_rate = models.FloatField(null=True, blank=True, default=None)
    def __str__(self):
        return self.name if self.name else f"Player {self.player_id}"
