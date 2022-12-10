from django.db import models
from datetime import datetime, date
import uuid


# For research only (default_group if not research mode)
class Group(models.Model):
  id = models.AutoField(primary_key=True, verbose_name='Group ID ')
  name = models.CharField(max_length=250, verbose_name='Group Name', unique=True)

  def __str__(self):
    return self.name

# For public/private lobbies 
class Room(models.Model):
  room_id =  models.AutoField(primary_key=True, verbose_name='Room ID')
  room_name = models.CharField(max_length=250, verbose_name='Room Name')
  group_name = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Group Name")
  
  password = models.CharField(max_length=250, verbose_name='Password', blank=True)
  is_research = models.BooleanField(default=True, verbose_name="Research")

  # Can use this to data to compare and check if a player hosted or not
  players = models.TextField(verbose_name='players', blank=True)
  host = models.TextField(verbose_name='host', blank=True)
  done_host_list = models.TextField(verbose_name='Done Hosting', blank=True)
  online = models.TextField(verbose_name='Online', blank=True)

  # Settings data
  arithmetic = models.TextField(verbose_name='Arithmetic', blank=True)
  difficulty = models.TextField(verbose_name='difficulty', blank=True)
  speed = models.TextField(verbose_name='Speed', blank=True)
  lvl = models.TextField(verbose_name='lvl', blank=True)

  # Active Room
  is_active = models.BooleanField(default=True, verbose_name="Active")

  def __str__(self):
    return self.room_name

  def get_players_count(self):
    return self.players.count()

  def chk_if_done_host(self, player):
    if player in self.host_list:
      return False
    else:
      return True

  def chk_if_all_player_done_hosting(self):
    if self.players == self.host_list:
      return True
    else:
      return False
  
