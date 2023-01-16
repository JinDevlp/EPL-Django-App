from django.shortcuts import render,redirect

from django.http import JsonResponse
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
            elif Team.objects.filter(teamnumber=teams_data.teamnumber).exists():
                Team.objects.filter(teamnumber=teams_data.teamnumber).update(
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

            elif Player.objects.filter(code=player_data.code).exists():
                Player.objects.filter(code=player_data.code).update(
                    code = l['id'],
                    name = l['name'],
                    position = l['position'],
                    dateofbirth = l['dateOfBirth'],
                    nationality = l['nationality'],
                    team = Team.objects.get(teamnumber = teams_data.teamnumber)
                    )

    # top scorers json
    topPlayers_response = requests.get(top_players,headers=headers)
    scorers_data = topPlayers_response.json()
    topPlayers = scorers_data['scorers']
    for i in topPlayers:
        Player.objects.filter(code=i['player']['id']).update(
                code=i['player']['id'],
                goals = i['goals'],
                assists = i['assists'],
                penalties = i['penalties'],
                top_scorer = True
            )

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
        if LeaderBoard.objects.filter(team=stats_data.team).exists():
            LeaderBoard.objects.filter(team=stats_data.team).update(
                position = i['position'],
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

    all_stats = LeaderBoard.objects.all().order_by('position')
    all_players = Player.objects.all().order_by('-goals')
    all_teams = Team.objects.all()


    return render(request, 'teams/home.html',{'all_stats':all_stats,'all_teams':all_teams,'all_players':all_players})


def viewTeam(request,pk):
    target_team = Team.objects.get(teamnumber=pk)
    players = Player.objects.all().order_by()


    return render(request, 'teams/team.html',{'target_team':target_team,'players':players})

