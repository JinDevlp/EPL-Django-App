from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from teams.models import Team, LeaderBoard
from player.models import Player
from match.models import Match, Score


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
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