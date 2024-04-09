from django.contrib import admin
from .models import Matches,Teams,Squad
# Register your models here.

@admin.register(Teams)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_id', 'name')


@admin.register(Matches)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_id', 'team_1','team_2','date','venue','status')

@admin.register(Squad)
class SquadAdmin(admin.ModelAdmin):
    list_display = ('team', 'player','role') 