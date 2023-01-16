from rest_framework.response import Response
from rest_framework.decorators import api_view

from teams.models import Team, LeaderBoard
from player.models import Player
from match.models import Match
from .serializers import TeamSerializer,TeamInfoSerializer,PlayerSerializer, LeaderBoardSerializer, TopScorerSerializer,MatchSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/teams'},
        {'GET': '/api/teams/teamnumber'},

        {'GET': '/api/matches'},
        {'GET': '/api/matches/code'},

        {'GET': '/api/leaderboard'},
        {'GET': '/api/top-scorer'},

        {'GET': '/api/players'},
        {'GET': '/api/players/code'},
    ]
    return Response(routes)

@api_view(['GET'])
def viewTeams(request):
    all_teams = Team.objects.all()

    team_serializer = TeamSerializer(all_teams,many=True)
    return Response(team_serializer.data)

@api_view(['GET'])
def viewTeam(request,pk):
    team = Team.objects.get(teamnumber=pk)
    team_serializer = TeamInfoSerializer(team,many=False)

    return Response(team_serializer.data)

@api_view(['GET'])
def viewPlayers(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def viewPlayer(request,pk):
    player = Player.objects.get(code=pk)
    serializer = PlayerSerializer(player,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def viewBoard(request):
    leader_board = LeaderBoard.objects.all()
    serializer = LeaderBoardSerializer(leader_board,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def viewTopScorers(request):
    top_scorer = Player.objects.filter(top_scorer=True)
    serializer = TopScorerSerializer(top_scorer,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def viewMatches(request):
    matches = Match.objects.all()
    serializer = MatchSerializer(matches,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewMatch(request,pk):
    matches = Match.objects.get(code=pk)
    serializer = MatchSerializer(matches,many=False)
    return Response(serializer.data)