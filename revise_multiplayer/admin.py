from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Admin Displays

class GroupAdmin(admin.ModelAdmin):
  list_display = ['name', 'id']

class RoomAdmin(admin.ModelAdmin):
  list_per_page = 15
  list_max_show_all = 50
  list_display = ['room_id','room_name','group_name','password','is_research','players','host','done_host_list','online','arithmetic','difficulty','speed','lvl']
  readonly_fields = ['room_id','password', 'is_research']

# class GameSettingAdmin(admin.ModelAdmin):
#   list_display = ['room', 'host', 'arithmetic', 'difficulty', 'speed', 'lvl']
#   readonly_fields = ['room', 'host', 'arithmetic', 'difficulty', 'speed', 'lvl']

# Register your models here.
admin.site.register(Group, GroupAdmin)
admin.site.register(Room, RoomAdmin)

