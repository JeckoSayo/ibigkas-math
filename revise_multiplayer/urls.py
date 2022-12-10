from django.urls import path
from . import views 

app_name = 'revise_multiplayer'

urlpatterns = [ 
  path("room-list/<uuid>", views.room_list, name="room_list"),
  path("room/<str:room_name>/<uuid>/", views.room, name="room"),
  path("room/<str:room_name>/<uuid>/gameplay/", views.multiplayer_gameplay, name="multiplayer_gameplay"),

  # Ajax
  path("multiPlayerSettingsAjax/", views.multiPlayerSettingsAjax, name="multiPlayerSettingsAjax"),
  # path("userGameResultsAjax/", views.userGameResults, name="userGameResultsAjax"),
]