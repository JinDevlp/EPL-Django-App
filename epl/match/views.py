from django.shortcuts import render
import requests
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from .models import Match, Score
from teams.models import Team

import environ
env = environ.Env()
environ.Env.read_env()
# Create your views here.
def viewMatches(request,*args):
    url = 'http://api.football-data.org/v4/competitions/PL/matches?season=2022'
    headers = { 'X-Auth-Token': env('TOKEN') }
    # matches json
    response = requests.get(url,headers=headers)
    matches_json = response.json()
    matches_list = matches_json['matches']

    for i in matches_list:
        if i['score']['winner']== 'HOME_TEAM':
            score_data = Score(
                matchid = i['id'],
                winner = Team.objects.get(teamnumber=i['homeTeam']['id'] ),
                fulltime_home = i['score']['fullTime']['home'],
                fulltime_away = i['score']['fullTime']['away'],
                halftime_home = i['score']['halfTime']['home'],
                halftime_away =i['score']['halfTime']['away']
            )
            if not Score.objects.filter(matchid=i['id']).exists():
                score_data.save()

        elif i['score']['winner']== 'AWAY_TEAM':
            score_data = Score(
            matchid = i['id'],
            winner = Team.objects.get(teamnumber=i['awayTeam']['id'] ),
            fulltime_home = i['score']['fullTime']['home'],
            fulltime_away = i['score']['fullTime']['away'],
            halftime_home = i['score']['halfTime']['home'],
            halftime_away =i['score']['halfTime']['away']
            )
            if not Score.objects.filter(matchid=i['id']).exists():
                score_data.save()

        elif i['score']['winner']== 'DRAW':
            score_data = Score(
            matchid = i['id'],
            winner = None,
            fulltime_home = i['score']['fullTime']['home'],
            fulltime_away = i['score']['fullTime']['away'],
            halftime_home = i['score']['halfTime']['home'],
            halftime_away =i['score']['halfTime']['away']
            )
            if not Score.objects.filter(matchid=i['id']).exists():
                score_data.save()

        elif i['score']['winner']== 'null':
            score_data = Score(
            matchid = i['id'],
            winner = None,
            fulltime_home = i['score']['fullTime']['home'],
            fulltime_away = i['score']['fullTime']['away'],
            halftime_home = i['score']['halfTime']['home'],
            halftime_away =i['score']['halfTime']['away']
            )
            if not Score.objects.filter(matchid=i['id']).exists():
                score_data.save()

        elif i['status'] == 'POSTPONED' or i['status'] == 'SCHEDULED' or i['status'] == 'TIMED':
            score_data = Score(
            matchid = i['id'],
            winner = None,
            fulltime_home = i['score']['fullTime']['home'],
            fulltime_away = i['score']['fullTime']['away'],
            halftime_home = i['score']['halfTime']['home'],
            halftime_away =i['score']['halfTime']['away']
            )
            if not Score.objects.filter(matchid=i['id']).exists():
                score_data.save()


        match_data = Match(
            code = i['id'],
            utcDate = i['utcDate'],
            status = i['status'],
            matchday = i['matchday'],
            homeTeam = Team.objects.get(teamnumber=i['homeTeam']['id'] ),
            awayTeam = Team.objects.get(teamnumber=i['awayTeam']['id'] ),
            final_score = Score.objects.get(matchid = score_data.matchid)
            )

        if not Match.objects.filter(code=match_data.code).exists():
            match_data.save()

        all_scores = Score.objects.all()
        all_matches = Match.objects.all().order_by('utcDate')

    return render(request, 'matches.html', {'all_scores':all_scores,'all_matches':all_matches})