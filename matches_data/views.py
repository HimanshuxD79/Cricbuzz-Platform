from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Matches, Teams ,Squad
from .serializers import MatchDetailSerializer,MatchesSerializer,SquadSerializer
from players_stats.models import Players
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from django.utils.decorators import method_decorator
# Create your views here.



class GetMatchesAPIView(APIView):
    authentication_classes =[]
    permission_classes = []
    def get(self, request):
        matches = Matches.objects.all()
        serializer = MatchesSerializer(matches, many=True)
        return Response({"matches": serializer.data})

class MatchesAPIView(APIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        team_1_name = request.data.get('team_1')
        team_2_name = request.data.get('team_2')
        date = request.data.get('date')
        venue = request.data.get('venue')

        if team_1_name == team_2_name:
            return Response({"message":"Both teams cannot be the same"},status=status.HTTP_400_BAD_REQUEST)

        try:
            team_1 = Teams.objects.get(name=team_1_name)

        except Teams.DoesNotExist:
            return Response({"message": "Team 1 does not exist"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            team_2 = Teams.objects.get(name=team_2_name)
        except Teams.DoesNotExist:
            return Response({"message": "Team 2 does not exist"}, status=status.HTTP_400_BAD_REQUEST)    

        match = Matches(team_1=team_1, team_2=team_2, date=date, venue=venue)
        match.save()

        return Response({"message": "Match created successfully", "match_id": match.match_id}, status=status.HTTP_201_CREATED)


class MatchDetailAPIView(APIView):
    def get(self, request, match_id):
        try:
            match = Matches.objects.get(match_id=match_id)
            serializer = MatchDetailSerializer(match)
            return Response(serializer.data)
        except Matches.DoesNotExist:
            return Response({'error': f'Match with ID {match_id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SquadCreateAPIView(APIView):
    authentication_classes =[TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, team_id):
        authentication_classes = [TokenAuthentication]
        permission_classes  = [IsAuthenticated]
        # Retrieve the team instance
        try:
            team = Teams.objects.get(team_id=team_id)
        except Teams.DoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve player details from request data
        name = request.data.get('name')
        role = request.data.get('role')

        # Check if the player exists
        try:
            player = Players.objects.get(name=name)
        except Players.DoesNotExist:
            return Response({"message": "Player not found"}, status=status.HTTP_404_NOT_FOUND)

        # Create squad instance
        squad = Squad(team=team, player=player, role=role)
        squad.save()

        # Serialize response data
        serializer = SquadSerializer(squad)

        return Response({"message": "Player added to squad successfully", "player_id": player.player_id}, status=status.HTTP_201_CREATED)