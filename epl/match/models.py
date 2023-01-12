from django.db import models
from teams.models import Team

# Create your models here.
class Score(models.Model):
    winner = models.ForeignKey(Team,on_delete=models.CASCADE, null=True, blank=True,related_name="winTeam")
    fulltime_home = models.IntegerField( blank=True, null=True )
    fulltime_away = models.IntegerField( blank=True, null=True )
    halftime_home = models.IntegerField( blank=True, null=True )
    halftime_away = models.IntegerField( blank=True, null=True )


class Match(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True )
    utcDate = models.CharField(max_length=255, blank=True, null=True )
    status = models.CharField(max_length=255, blank=True, null=True )
    matchday = models.IntegerField( blank=True, null=True )
    homeTeam = models.ForeignKey(Team,on_delete=models.CASCADE, null=True, blank=True,related_name="homeTeam")
    awayTeam = models.ForeignKey(Team,on_delete=models.CASCADE, null=True, blank=True,related_name="awayTeam")
    score = models.ForeignKey(Score,on_delete=models.CASCADE, null=True, blank=True,related_name="score")