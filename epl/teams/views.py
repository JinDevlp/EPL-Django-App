from django.shortcuts import render,redirect

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
    board = 'http://api.football-data.org/v4/competitions/PL/standings'
    team_info = 'http://api.football-data.org/v4/competitions/PL/teams'
    top_players = 'http://api.football-data.org/v4/competitions/PL/scorers'
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
            all_teams = Team.objects.all()

            player_data =Player(
                code = l['id'],
                name = l['name'],
                position = l['position'],
                dateofbirth = l['dateOfBirth'],
                nationality = l['nationality'],
                team = Team.objects.get(teamnumber = teams_data.teamnumber)
                )
            if not Player.objects.filter(code=player_data.code).exists():
                player_data.save()

    # top scorers json
    topPlayers_response = requests.get(top_players,headers=headers)
    scorers_data = topPlayers_response.json()
    topPlayers = scorers_data['scorers']
    for i in topPlayers:
        add_info_player = Player.objects.get(code=i['player']['id'])
        if i['player']['id'] == int(add_info_player.code):
            print(add_info_player)
            add_info_player.goals = i['goals']
            add_info_player.assists = i['assists']
            add_info_player.penalties = i['penalties']
            add_info_player.top_scorer = True
            print(add_info_player.goals)
            add_info_player.save()

    all_players = Player.objects.all().order_by('-goals')

    # Leader board
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
        all_stats = LeaderBoard.objects.all().order_by('position')

    return render(request, 'home.html',{'all_stats':all_stats,'all_teams':all_teams,'all_players':all_players})


def viewTeam(request,pk):
    target_team = Team.objects.filter(teamnumber=pk)
    players = Player.objects.all().order_by()

    return render(request, 'team.html',{'target_team':target_team,'players':players})

