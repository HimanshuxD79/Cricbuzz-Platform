from rest_framework import serializers
from .models import Matches ,Teams ,Squad
from players_stats.models import Players
class MatchesSerializer(serializers.ModelSerializer):
    team_1_name = serializers.SerializerMethodField()
    team_2_name = serializers.SerializerMethodField()
    def get_team_1_name(self, obj):
        return obj.team_1.name if obj.team_1 else None

    def get_team_2_name(self, obj):
        return obj.team_2.name if obj.team_2 else None
    class Meta:
        model = Matches
        fields = ('match_id', 'team_1_name', 'team_2_name', 'date', 'venue')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = ('player_id', 'name')

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ('name',)

class SquadSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()

    class Meta:
        model = Squad
        fields = ('player',)

class MatchDetailSerializer(serializers.ModelSerializer):
    team_1 = TeamSerializer()
    team_2 = TeamSerializer()
    squads = serializers.SerializerMethodField()

    class Meta:
        model = Matches
        fields = ('match_id', 'team_1', 'team_2', 'date', 'venue', 'status', 'squads')

    def get_squads(self, obj):
        team_1_squads = Squad.objects.filter(team=obj.team_1)
        team_2_squads = Squad.objects.filter(team=obj.team_2)
        team_1_data = SquadSerializer(team_1_squads, many=True).data
        team_2_data = SquadSerializer(team_2_squads, many=True).data
        return {'team_1': team_1_data, 'team_2': team_2_data}