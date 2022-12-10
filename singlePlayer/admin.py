from django.contrib import admin
from .models import *

# Register your models here.


class GameSettingAdmin(admin.ModelAdmin):
  list_display = ['setting_id', 'player', 'arithmetic', 'difficulty', 'speed', 'lvl']
  readonly_fields = ['setting_id','player', 'arithmetic', 'difficulty', 'speed', 'lvl']

  list_per_page = 15
  list_max_show_all = 50

admin.site.register(GameSetting, GameSettingAdmin)