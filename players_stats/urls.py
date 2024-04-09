from django.urls import path
from .views import PlayerStatsAPIView

urlpatterns = [
    path('players/<str:player_id>/stats', PlayerStatsAPIView.as_view()),
]