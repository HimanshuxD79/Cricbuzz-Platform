from django.contrib import admin
from .models import Players
# Register your models here.
@admin.register(Players)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id', 'name', 'matches_played', 'runs', 'average', 'strike_rate')