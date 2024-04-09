from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Players
from .serializers import PlayerStatsSerializer
# Create your views here.

class PlayerStatsAPIView(APIView):
    def get(self,request,player_id):
        try:
            player = Players.objects.get(player_id=player_id)
            serializer = PlayerStatsSerializer(player)
            return Response(serializer.data)
        except Players.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)    