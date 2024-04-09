from django.urls import path
from .views import MatchesAPIView,MatchDetailAPIView,SquadCreateAPIView

urlpatterns = [
    path('matches', MatchesAPIView.as_view()),
    path('matches/<int:match_id>', MatchDetailAPIView.as_view()),
    path('teams/<int:team_id>/squad/', SquadCreateAPIView.as_view(), name='add_to_squad'),
]