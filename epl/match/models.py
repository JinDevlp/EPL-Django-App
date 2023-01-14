from django.db import models
from teams.models import Team
import uuid

# Create your models here.
class Score(models.Model):
    winner = models.ForeignKey(Team,on_delete=models.CASCADE, null=True, blank=True,related_name="winTeam")
    fulltime_home = models.IntegerField( blank=True, null=True )
    fulltime_away = models.IntegerField( blank=True, null=True )
    halftime_home = models.IntegerField( blank=True, null=True )
    halftime_away = models.IntegerField( blank=True, null=True )
    matchid = models.CharField(max_length=255, blank=True, null=True )


class Match(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True )
    utcDate = models.CharField(max_length=255, blank=True, null=True )
    status = models.CharField(max_length=255, blank=True, null=True )
    matchday = models.IntegerField( blank=True, null=True )
    homeTeam = models.ForeignKey(Team,on_delete=models.CASCADE, null=True, blank=True,related_name="home")
    awayTeam = models.ForeignKey(Team,on_delete=models.CASCADE, null=True, blank=True,related_name="away")
    final_score = models.ForeignKey(Score,on_delete=models.CASCADE, null=True, blank=True)