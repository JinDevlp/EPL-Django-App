from django.shortcuts import render,redirect

from django.core.exceptions import ObjectDoesNotExist
import itertools

from .models import Team, LeaderBoard
from player.models import Player

import requests

import environ
env = environ.Env()
environ.Env.read_env()
# Create your views here.

"""Get Team info with Squad and Standings for 2022-2023 EPL season"""
def home(request):
    all_teams = {}
    board = 'http://api.football-data.org/v4/competitions/PL/standings'
    team_info = 'http://api.football-data.org/v4/competitions/PL/teams'
    headers = { 'X-Auth-Token': env('TOKEN') }

    # team_info json
    teaminfo_response = requests.get(team_info,headers=headers)
    team_data = teaminfo_response.json()
    teams = team_data['teams']

    for i  in teams:
        squads = i['squad']
        for l in squads:
            teams_data = Team(
                areacode = i['area']['id'],
                teamnumber = i['id'],
                teamname = i['name'],
                shortname = i['shortName'],
                tla = i['tla'],
                crest = i['crest'],
                website = i['website'],
                clubColors = i['clubColors'],
                coach = i['coach']['name'],
            )
            if not Team.objects.filter(teamnumber=teams_data.teamnumber).exists():
                teams_data.save()
                print(teams_data)

            player_data =Player(
                code = l['id'],
                name = l['name'],
                position = l['position'],
                dateofbirth = l['dateOfBirth'],
                nationality = l['nationality'],
                team = Team.objects.get(teamnumber = teams_data.teamnumber)
                )

    # for l in squads:
    #     player_data =Player(
    #         code = l['id'],
    #         name = l['name'],
    #         position = l['position'],
    #         dateofbirth = l['dateOfBirth'],
    #         nationality = l['nationality'],
    #         team = Team.objects.get(teamnumber = teams_data.teamnumber)
    #     )
            if not Player.objects.filter(code=player_data.code).exists():
                player_data.save()

    # board json
    board_response = requests.get(board, headers=headers)
    total_data = board_response.json()
    positions = total_data['standings'][0]['table']

    for i in positions:
        stats_data = LeaderBoard(
            position = i['position'],
            team = Team.objects.get(teamnumber = i['team']['id']),
            playedgames = i['playedGames'],
            form = i['form'],
            won = i['won'],
            draw = i['draw'],
            lost = i['lost'],
            points = i['points'],
            goalsfor = i['goalsFor'],
            goalsagainst = i['goalsAgainst'],
            goalsdifference = i['goalDifference']
        )
        if not LeaderBoard.objects.filter(team=stats_data.team).exists():
            stats_data.save()
        print(stats_data)
        all_stats = LeaderBoard.objects.all().order_by('position')

    return render(request, 'home.html',{'all_stats':all_stats,'all_teams':all_teams})


"""Get quick info on teams"""
# for i in teams:
    #     team_data = Team(
    #         teamnumber =  i['team']['id'],
    #         teamname = i['team']['name'],
    #         shortname= i['team']['shortName'],
    #         tla = i['team']['tla'],
    #         crest = i['team']['crest']
    #     )
    #     if not Team.objects.filter(teamnumber=team_data.teamnumber).exists():
    #         team_data.save()
    # all_teams = Team.objects.all().order_by('-id')
