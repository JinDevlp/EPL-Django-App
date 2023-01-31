from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from teams.models import Team, LeaderBoard
from player.models import Player
from match.models import Match, Score
from django.contrib.auth.models import User
from user.models import Profile


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False,required=False)
    team = TeamSerializer(many=False,required=False)

    class Meta:
        model = Profile
        fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False,required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False)

    class Meta:
        model = Player
        fields = '__all__'

class TeamInfoSerializer(serializers.ModelSerializer):
    players = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'

    # ForeignKey query
    def get_players(self,obj):
        players = obj.player_set.all()
        serializer = PlayerSerializer(players,many=True)
        return serializer.data

class LeaderBoardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=False)
    class Meta:
        model = LeaderBoard
        fields = '__all__'

class TopScorerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class ScoreSerializer(serializers.ModelSerializer):
    winner = TeamSerializer(many=False)
    class Meta:
        model = Score
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    homeTeam = TeamSerializer(many=False)
    awayTeam = TeamSerializer(many=False)
    final_score = ScoreSerializer(many=False)
    class Meta:
        model = Match
        fields = '__all__'
