from rest_framework import serializers
from .models import Players

class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Players
        fields= ('player_id', 'name', 'matches_played', 'runs', 'average', 'strike_rate')