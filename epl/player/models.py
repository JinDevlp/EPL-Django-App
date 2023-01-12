from django.db import models
from teams.models import Team
# Create your models here.

class Player(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    dateofbirth = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True,related_name="playerteam")
    goals = models.IntegerField( blank=True, null=True )
    assists = models.IntegerField( blank=True, null=True )
    penalties = models.IntegerField( blank=True, null=True )
    top_scorer = models.BooleanField(default=False, blank=True, null=True )

    def __str__(self):
        return self.name