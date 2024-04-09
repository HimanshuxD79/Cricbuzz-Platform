from django.db import models
from players_stats.models import Players
from django.utils import timezone
from datetime import datetime
# Create your models here.
class Teams(models.Model):
    team_id = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=256,null=True, blank=True,default=None)

    def __str__(self):
        return self.name if self.name else f"Team {self.team_id}"


    
class Matches(models.Model):
    MATCH_STATUS_CHOICES = (
        ('upcoming', 'Upcoming'),
        ('current', 'Current'),
        ('finished', 'Finished'),
    )
    match_id = models.AutoField(primary_key=True)
    team_1 = models.ForeignKey(Teams,on_delete=models.CASCADE,related_name='team_1_matches')
    team_2 = models.ForeignKey(Teams,on_delete=models.CASCADE,related_name='team_2_matches')
    date = models.DateField()
    venue = models.CharField(max_length=256,null=True,blank=True)
    status = models.CharField(max_length=20, choices=MATCH_STATUS_CHOICES, default='upcoming', editable=False)

    def save(self, *args, **kwargs):
        current_date = timezone.now().date()
        self_date = datetime.strptime(self.date, '%Y-%m-%d').date()
        if self_date > current_date:
            self.status = 'upcoming'
        elif self_date == current_date:
            self.status = 'current'
        else:
            self.status = 'finished'

        super().save(*args, **kwargs)
    

class Squad(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    role = models.CharField(max_length=256,null=True,blank=True,default=None)