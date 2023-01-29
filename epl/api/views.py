from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import mixins, generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from teams.models import Team, LeaderBoard
from user.models import Profile
from player.models import Player
from match.models import Match, Score
from rest_framework.views import APIView
from django.http import Http404
from .serializers import TeamSerializer,TeamInfoSerializer,PlayerSerializer, LeaderBoardSerializer, TopScorerSerializer,UserSerializer,MatchSerializer, ProfileSerializer, ScoreSerializer

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

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer()

class ProfileList(generics.ListAPIView
                    ):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrReadOnly,)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrReadOnly,)

class TeamsList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# ID as pk
class TeamsDetail(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamInfoSerializer # Returns Team Info with Players Info

# If want to use Teamnumber as pk
"""class TeamsDetail(APIView):
    def get_object(self,pk): # Get Team object
        try:
            return Team.objects.get(teamnumber=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self,request, pk,format=None): # Returns Team info with players
        team = self.get_object(pk)
        team_serializer = TeamInfoSerializer(team)
        return Response(team_serializer.data)"""

class MatchesList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class MatchDetail(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer # Returns Match Info with Score Info

class PlayersList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayersDetail(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class LeaderboardList(generics.ListCreateAPIView):
    queryset = LeaderBoard.objects.all()
    serializer_class = LeaderBoardSerializer

class TopScorerList(generics.ListCreateAPIView):
    queryset = Player.objects.filter(top_scorer=True)
    serializer_class = TopScorerSerializer

@api_view(['GET'])
def matchDay(request,pk):
    matches = Match.objects.filter(matchday=pk)

    serializer = MatchSerializer(matches,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def addFavTeam(request,pk):
   profile = Profile.objects.get(id=pk)
   profile_serializer = ProfileSerializer(profile,many=False)

   data = request.data
   team = Team.objects.get(id= data['fav_team']) # Get Team Object according to teamname
   if profile.fav_team == None:
       profile.fav_team = team
       profile.save()
   else:
       return Response("You already have a favorite team", status = status.HTTP_400_BAD_REQUEST)

   return Response(profile_serializer.data, status= status.HTTP_202_ACCEPTED)

@api_view(['DELETE'])
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

