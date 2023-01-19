from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from teams.models import Team, LeaderBoard
from user.models import Profile
from player.models import Player
from match.models import Match, Score
from rest_framework.views import APIView
from .serializers import TeamSerializer,TeamInfoSerializer,PlayerSerializer, LeaderBoardSerializer, TopScorerSerializer,MatchSerializer, ProfileSerializer, ScoreSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/teams'},
        {'GET': '/api/teams/teamnumber'},

        {'GET': '/api/matches'},
        {'GET': '/api/matches/matchdays/matchday'},
        {'GET': '/api/matches/matchcode'},
        {'GET': '/api/matches/matchcode/scores'},

        {'GET': '/api/leaderboard'},
        {'GET': '/api/top-scorer'},

        {'GET': '/api/players'},
        {'GET': '/api/players/playercode'},

        {'GET': '/api/profiles'},
        {'GET': '/api/profiles/id'},

        {'POST': '/api/profiles/id/teams/teamnumber/add'},
        {'PATCH': '/api/profiles/id/teams/teamnumber/remove'},

    ]
    return Response(routes)

@api_view(['GET'])
def viewProfiles(request):
    profiles = Profile.objects.all()

    profile_serializer = ProfileSerializer(profiles,many=True)
    return Response(profile_serializer.data)

@api_view(['GET'])
def viewProfile(request,pk):
    profile = Profile.objects.get(id=pk)

    profile_serializer = ProfileSerializer(profile,many=False)
    return Response(profile_serializer.data)

class TeamsList(APIView):
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
    match = Match.objects.get(code=pk)
    serializer = MatchSerializer(match,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def matchDay(request,pk):
    matches = Match.objects.filter(matchday=pk)

    serializer = MatchSerializer(matches,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewMatchScores(request,pk):
    match = Match.objects.get(code=pk) #Get Single Match obj with Match code
    score = Score.objects.get(matchid=match.code) # Get Score obj from that Match obj

    serializer = ScoreSerializer(score,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addFavTeam(request,pk):
   profile = Profile.objects.get(id=pk)
   profile_serializer = ProfileSerializer(profile,many=False)

   data = request.data
   team = Team.objects.get(teamnumber= data['fav_team']) # Get Team Object according to teamname
   if profile.fav_team == None:
       profile.fav_team = team
       profile.save()
   else:
       return Response("You already have a favorite team", status = status.HTTP_400_BAD_REQUEST)

   return Response(profile_serializer.data, status= status.HTTP_202_ACCEPTED)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def removeFavTeam(request,pk):
   profile = Profile.objects.get(id=pk)
   profile_serializer = ProfileSerializer(profile,many=False)

   if profile.fav_team:
       profile.fav_team = None
       profile.save()
   else:
       return Response("You don't have a favorite team", status = status.HTTP_400_BAD_REQUEST)


   return Response(profile_serializer.data, status= status.HTTP_202_ACCEPTED)

