# from email import message
import json 
from channels.generic.websocket import WebsocketConsumer 
from asgiref.sync import async_to_sync
from revise_multiplayer.models import * 

class MultiplayerGameplay(WebsocketConsumer):
  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)
    self.room_name = None
    self.room_group_name = None
    self.room = None

  def connect(self):

    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = f'channel_group_{self.room_name}'
    self.room = Room.objects.get(room_name=self.room_name)

    # connection has to be accepted
    self.accept()

    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name
    )

    # send the user list to the newly joined user
    self.send(json.dumps({
      'type': 'player_list',
      'message': self.room.online,
    }))
  
  def disconnect(self, close_code):
    # print("disconnected")
    # print("SELF: ", self.scope)
    # print("deleting all online")
    self.room.online = ''
    self.room.save()

    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'disconnection',
        'message': "Websocket disconnected"
      }
    )

    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'player_list',
        'message': self.room.online
      }
    )

    async_to_sync(self.channel_layer.group_discard)(
      self.room_group_name,
      self.channel_name,
    )

  def receive(self, text_data=None, bytes_data=None):
    def add_player_to_online(self, player_name):
      # print("Adding Player: ", player_name)
      players_in_rooms = self.room.online
      players_in_rooms += (" " + player_name)
      self.room.online = players_in_rooms
      self.room.save()
    
    # Updating the variable
    self.room = Room.objects.get(room_name=self.room_name)

    text_data_json = json.loads(text_data)
    # print("data received: " , text_data_json)
    
    player_name = text_data_json['player_name']
    status = text_data_json['status']

    if player_name not in self.room.online and status == "add":
      add_player_to_online(self, player_name)

      async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
        {
          'type': 'player_list',
          'message': self.room.online
      })

    if player_name not in self.room.online and status == "remove":
      
      add_player_to_online(self, player_name)
      # print("Remaining Player: ", player_name)

      async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'player_list',
        'message': self.room.online
      }
    )

  def player_list(self, event):
    self.send(text_data=json.dumps(event))

  def disconnection(self, event):
    self.send(text_data=json.dumps(event))


class MultiplayerSettings(WebsocketConsumer):

  def __init__(self, *args, **kwargs):
    super().__init__(args, kwargs)
    self.room_name = None
    self.room_group_name = None
    self.room = None

  def connect(self):

    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = f'channel_group_{self.room_name}'
    self.room = Room.objects.get(room_name=self.room_name)

    # connection has to be accepted
    self.accept()

    async_to_sync(self.channel_layer.group_add)(
      self.room_group_name,
      self.channel_name
    )

    # send the user list to the newly joined user
    self.send(json.dumps({
      'type': 'player_list',
      'message': self.room.online,
    }))
  
  def disconnect(self, close_code):
    # print("disconnected")
    # print("SELF: ", self.scope)
    # print("deleting all online")
    self.room.online = ''
    self.room.save()

    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'disconnection',
        'message': "Websocket disconnected"
      }
    )

    async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'player_list',
        'message': self.room.online
      }
    )

    async_to_sync(self.channel_layer.group_discard)(
      self.room_group_name,
      self.channel_name,
    )
  
  def receive(self, text_data=None, bytes_data=None):
    def add_player_to_online(self, player_name):
      # print("Adding Player: ", player_name)
      players_in_rooms = self.room.online
      players_in_rooms += (" " + player_name)
      self.room.online = players_in_rooms
      self.room.save()
    
    # Updating the variable
    self.room = Room.objects.get(room_name=self.room_name)

    text_data_json = json.loads(text_data)
    # print("data received: " , text_data_json)
    
    player_name = text_data_json['player_name']
    status = text_data_json['status']

    if status == "game_start": 
    
      async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
        {
          'type': 'redirect_to_gameplay',
          'message': "gameplay/"
      })

    if player_name not in self.room.online and status == "add":
      add_player_to_online(self, player_name)

      async_to_sync(self.channel_layer.group_send)(
        self.room_group_name,
        {
          'type': 'player_list',
          'message': self.room.online
      })

    if player_name not in self.room.online and status == "remove":
      
      add_player_to_online(self, player_name)
      # print("Remaining Player: ", player_name)

      async_to_sync(self.channel_layer.group_send)(
      self.room_group_name,
      {
        'type': 'player_list',
        'message': self.room.online
      }
    )

  
  def player_list(self, event):
    self.send(text_data=json.dumps(event))

  def disconnection(self, event):
    self.send(text_data=json.dumps(event))

  def redirect_to_gameplay(self, event):
    self.send(text_data=json.dumps(event))