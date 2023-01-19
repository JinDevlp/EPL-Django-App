from django.shortcuts import render
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Match, Score
from teams.models import Team

import environ
env = environ.Env()
environ.Env.read_env()
# Create your views here.

def viewMatches(request):
    url = 'http://api.football-data.org/v4/competitions/PL/matches?season=2022'
    headers = { 'X-Auth-Token': env('TOKEN') }
    # matches json
    response = requests.get(url,headers=headers)
    matches_json = response.json()
    matches_list = matches_json['matches']

    for i in matches_list:
        if i['score']['winner']== 'HOME_TEAM':
            Score.objects.update_or_create(
                matchid = i['id'],
                winner = Team.objects.get(teamnumber=i['homeTeam']['id'] ),
                fulltime_home = i['score']['fullTime']['home'],
                fulltime_away = i['score']['fullTime']['away'],
                halftime_home = i['score']['halfTime']['home'],
                halftime_away =i['score']['halfTime']['away']
            )

        elif i['score']['winner']== 'AWAY_TEAM':
            Score.objects.update_or_create(
            matchid = i['id'],
            winner = Team.objects.get(teamnumber=i['awayTeam']['id'] ),
            fulltime_home = i['score']['fullTime']['home'],
            fulltime_away = i['score']['fullTime']['away'],
            halftime_home = i['score']['halfTime']['home'],
            halftime_away =i['score']['halfTime']['away']
            )

        elif i['score']['winner']== 'DRAW':
            Score.objects.update_or_create(
            matchid = i['id'],
            winner = None,
            fulltime_home = i['score']['fullTime']['home'],
            fulltime_away = i['score']['fullTime']['away'],
            halftime_home = i['score']['halfTime']['home'],
            halftime_away =i['score']['halfTime']['away']
            )

        elif i['score']['winner']== 'null':
            Score.objects.update_or_create(
            matchid = i['id'],
            winner = None,
            fulltime_home = i['score']['fullTime']['home'],
            fulltime_away = i['score']['fullTime']['away'],
            halftime_home = i['score']['halfTime']['home'],
            halftime_away =i['score']['halfTime']['away']
            )

        elif i['status'] == 'POSTPONED' or i['status'] == 'SCHEDULED' or i['status'] == 'TIMED':
            Score.objects.update_or_create(
            matchid = i['id'],
            winner = None,
            fulltime_home = i['score']['fullTime']['home'],
            fulltime_away = i['score']['fullTime']['away'],
            halftime_home = i['score']['halfTime']['home'],
            halftime_away =i['score']['halfTime']['away']
            )

        Match.objects.update_or_create(
            code = i['id'],
            utcDate = i['utcDate'],
            status = i['status'],
            matchday = i['matchday'],
            homeTeam = Team.objects.get(teamnumber=i['homeTeam']['id'] ),
            awayTeam = Team.objects.get(teamnumber=i['awayTeam']['id'] ),
            final_score = Score.objects.get(matchid = i['id'])
            )

        all_scores = Score.objects.all()
        all_matches = Match.objects.all().order_by('-matchday')

        paginator = Paginator(all_matches,3)
        page = request.GET.get('page')
        matches = paginator.get_page(page)

    return render(request, 'matches.html', {'all_scores':all_scores,'all_matches':all_matches,'paginator':paginator,'page':page,'matches':matches})