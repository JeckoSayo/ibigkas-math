from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Assessment.models import * 
from revise_multiplayer.models import *

import json

# Internal Imports
from singlePlayer import utility as utils
from singlePlayer import filter_question_data as filter_qa

def room_list(request, uuid):

  player = Player.objects.get(uuid=uuid)
  rooms = Room.objects.all()
  room_names = []
  for i in range (len(rooms)):
    room_names.append(rooms[i].room_name)

  out = {
    'player': player,
    'rooms': room_names
  }

  return render(request, "revise_multiplayer/room.html", out)

def room(request, uuid, room_name):

  room, created = Room.objects.get_or_create(room_name=room_name)
  player = Player.objects.get(uuid=uuid)

  host = assign_or_get_host(player, room)

  out = {
    "room": room,
    'player': player,
    'host': host
  }
  
  return render(request, "revise_multiplayer/room-settings.html", out)

def assign_or_get_host(player, room):
  if room.host == "" or room.host == None:
    
    if player.username not in room.done_host_list:
      room.host = player.username
      room.save()
    else:
      print("This player is already done hosting: ", player.username )

  return room.host

def multiPlayerSettingsAjax(request):
  if request.method == 'POST':
    room_name = request.POST['room_name']
    arithmeticResults = request.POST['arithmeticResults']
    difficultyResults = request.POST['difficultyResults']
    year_level = request.POST['year_level']
    speed = request.POST['speed']
    # studentUUID = request.POST['studentUUID']

    def newFormat(s):
      s = s.translate({ord('['): None})
      s = s.translate({ord(']'): None})
      s = s.translate({ord('"'): None})
      return s
    
    arithmeticResults = newFormat(arithmeticResults)
    difficultyResults = newFormat(difficultyResults)
    
    if speed == "medium-two":
      speed = "medium"

    settings = {
      'arithmetic' : arithmeticResults,
      'lvl' : year_level,
      'speed' : speed,
      'difficulty' : difficultyResults
    }

    print("Settings:", settings)

    room_obj = Room.objects.get(room_name=room_name)

    curr_arithmetic = room_obj.arithmetic
    curr_difficulty = room_obj.difficulty
    curr_speed = room_obj.speed
    curr_lvl = room_obj.lvl

    room_obj.arithmetic = curr_arithmetic + ", " + arithmeticResults
    room_obj.difficulty = curr_difficulty + ", " + difficultyResults
    room_obj.speed = curr_speed + ", " + speed
    room_obj.lvl = curr_lvl + ", " + year_level
    room_obj.save()

    return HttpResponse("gameplay/")

def multiplayer_gameplay(request, room_name, uuid): 

  player = Player.objects.get(uuid=uuid)
  room = Room.objects.get(room_name=room_name)
  setting_entry = Multiplayer_Setting(
    room.arithmetic.split(", ")[-1],
    room.difficulty.split(", ")[-1],
    room.speed.split(", ")[-1],
    room.lvl.split(", ")[-1]
  )
  settings = utils.user_input(setting_entry)

  data = filter_qa.filter_question_dataset(settings)
  game_round_state = utils.init_game_round_variables()

  del setting_entry

  out = {
    "player": player,
    "room_name": room_name,
    "settings": settings,  
    "json_settings": json.dumps(settings),
    "json_game_round_state": json.dumps(game_round_state),
    "json_data" : json.dumps(data) 
  }

  return render(request, "revise_multiplayer/gameplay.html", out)

class Multiplayer_Setting:
  def __init__(self, arithmetic, difficulty, speed, lvl):
    self.arithmetic = arithmetic
    self.difficulty = difficulty
    self.speed = speed
    self.lvl = lvl