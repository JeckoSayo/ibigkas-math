from django.urls import path
from . import views 

app_name = 'singlePlayer'

urlpatterns = [ 
    path("menu-single-player/<uuid>/", views.singlePlayerMenu, name="singlePlayerMenu"),
    path("settings/<uuid>/", views.singlePlayerSettings, name="singlePlayerSettings"),
    path("how-to-play/", views.singlePlayerHowToPlay, name="HowToPlay"),
    path("game-play/<pk>/", views.singlePlayerGamePlay, name="gameplay"),

    # Ajax
    path("singlePlayerSettingsAjax/", views.singlePlayerSettingsAjax, name="singlePlayerSettingsAjax"),
    path("userGameResultsAjax/", views.userGameResults, name="userGameResultsAjax"),

]