from django.urls import path
from .views import MatchesAPIView,MatchDetailAPIView,SquadCreateAPIView,GetMatchesAPIView

urlpatterns = [
    path('addmatches', MatchesAPIView.as_view()),
    path('matches',GetMatchesAPIView.as_view()),
    path('matches/<int:match_id>', MatchDetailAPIView.as_view()),
    path('teams/<int:team_id>/squad/', SquadCreateAPIView.as_view(), name='add_to_squad'),
]