from django.urls import re_path
from .import consumers

websocket_urlspatterns = [
  re_path(r'ws/settings/(?P<room_name>\w+)/$', consumers.MultiplayerSettings.as_asgi()),
  re_path(r'ws/gameplay/(?P<room_name>\w+)/$', consumers.MultiplayerGameplay.as_asgi()),
]