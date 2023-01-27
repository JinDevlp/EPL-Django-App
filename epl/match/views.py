from django.shortcuts import render
import requests
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Match, Score
from teams.models import Team

import environ
env = environ.Env()
environ.Env.read_env()
# Create your views here.

def viewMatches(request):
    url = 'http://api.football-data.org/v4/competitions/PL/matches'
    headers = { 'X-Auth-Token': env('TOKEN') }
    # matches json
    response = requests.get(url,headers=headers)
    matches_json = response.json()
    matches_list = matches_json['matches']

    for i in matches_list:
        if i['score']['winner'] == "HOME_TEAM":
            obj, created = Score.objects.update_or_create(
                matchid = i['id'],
                    winner = Team.objects.get(teamnumber=i['homeTeam']['id']),
                    fulltime_home = i['score']['fullTime']['home'],
                    fulltime_away = i['score']['fullTime']['away'],
                    halftime_home = i['score']['halfTime']['home'],
                    halftime_away =i['score']['halfTime']['away'],)

        elif i['score']['winner'] == "AWAY_TEAM":
            obj, created = Score.objects.update_or_create(
                matchid = i['id'],
                    winner = Team.objects.get(teamnumber=i['awayTeam']['id']),
                    fulltime_home = i['score']['fullTime']['home'],
                    fulltime_away = i['score']['fullTime']['away'],
                    halftime_home = i['score']['halfTime']['home'],
                    halftime_away =i['score']['halfTime']['away'],)

        elif i['score']['winner'] == "DRAW":
            obj, created = Score.objects.update_or_create(
                matchid = i['id'],
                    winner = None,
                    fulltime_home = i['score']['fullTime']['home'],
                    fulltime_away = i['score']['fullTime']['away'],
                    halftime_home = i['score']['halfTime']['home'],
                    halftime_away =i['score']['halfTime']['away'],)

        elif i['status']== 'TIMED' or i['status']== 'SCHEDULED' or i['status']== 'POSTPONED' :
            obj, created = Score.objects.update_or_create(
                matchid = i['id'],
                    winner = None,
                    fulltime_home = i['score']['fullTime']['home'],
                    fulltime_away = i['score']['fullTime']['away'],
                    halftime_home = i['score']['halfTime']['home'],
                    halftime_away =i['score']['halfTime']['away'],)

        obj, created = Match.objects.update_or_create(
            code = i['id'],
            final_score = Score.objects.get(matchid = i['id']),
            utcDate = i['utcDate'],
            status = i['status'],
            matchday = i['matchday'],
            homeTeam =  Team.objects.get(teamnumber=i['homeTeam']['id'] ),
            awayTeam = Team.objects.get(teamnumber=i['awayTeam']['id'] ),
        )

        all_scores = Score.objects.all()
        all_matches = Match.objects.all().order_by('-matchday')

    return render(request, 'matches.html', {'all_scores':all_scores,'all_matches':all_matches,'count':range(1,39)})

def viewMatch(request,day):
    if 'day' in request.POST:
        data = request.POST['day']
        matchObj = Match.objects.filter(matchday=data)

    all_matches = Match.objects.all()

    return render(request, 'match.html', {'matchObj':matchObj,'all_matches':all_matches,'data':data,'count':range(1,39)})