from django.db import models
# Create your models here.


class Team(models.Model):
    areacode = models.CharField(max_length=255, blank=True, null=True )
    teamnumber = models.CharField(unique=True,max_length=255, blank=True, null=True )
    teamname = models.CharField(max_length=255, blank=True, null=True )
    shortname = models.CharField(max_length=255, blank=True, null=True )
    tla = models.CharField(max_length=255, blank=True, null=True )
    crest = models.CharField(max_length=255, blank = True, null = True)
    website = models.CharField(max_length=255, blank = True, null = True)
    clubColors = models.CharField(max_length=255, blank = True, null = True)
    coach = models.CharField(max_length=255, blank = True, null = True)


    def __str__(self):
        return self.teamname

class LeaderBoard(models.Model):
    position = models.IntegerField( blank=True, null=True )
    team = models.OneToOneField(Team, on_delete=models.CASCADE, null=True, blank=True,related_name="lbteam")
    playedgames = models.IntegerField( blank=True, null=True )
    form = models.CharField(max_length=255, blank=True, null=True )
    won = models.IntegerField( blank=True, null=True )
    draw = models.IntegerField( blank=True, null=True )
    lost = models.IntegerField( blank=True, null=True )
    points = models.IntegerField( blank=True, null=True )
    goalsfor = models.IntegerField( blank=True, null=True )
    goalsagainst = models.IntegerField( blank=True, null=True )
    goalsdifference = models.IntegerField( blank=True, null=True )

    def __int__(self):
        return (self.position)


