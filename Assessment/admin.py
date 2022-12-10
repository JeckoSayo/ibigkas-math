from itertools import count
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.



class PreTestAdmin(admin.ModelAdmin):
  list_display = ['operator', 'q1', 'q2','answer']
  list_filter = ('operator', 'answer')

  fieldsets = (
        ('Pre Test Questions',{
            'fields': ('operator', ('q11', 'q1'), ('q22', 'q2'),'answer'),
        }),
    )

class PersonalityTestAdmin(ImportExportModelAdmin):
  # line_numbering = 0
  list_display = ['questions','id']
  search_fields = ['questions']
  import_id_fields = ('questions',)

  # To add pagination at django admin
  list_per_page = 15
  list_max_show_all = 50

  # def line_number(self, obj):
  #   count = PersonalityTest.objects.all().count() + 1
  #   # self.line_numbering += count
  #   if self.line_numbering < count:
  #       self.line_numbering += 1
  #   else:
  #       self.line_numbering = 1
  #   return self.line_numbering

  # line_number.short_description = '#'
class ResearchAdmin(admin.ModelAdmin): 
  list_display = ['Research', 'research_mode']

  def Research(self, obj):
    return "Research Mode"
    
  Research.short_description = 'Research Status'

  # This will help you to disbale add functionality
  # def has_add_permission(self, request):
  #   return False
    
  # This will help you to disable delete functionality
  # def has_delete_permission(self, request, obj=None):
  #       return False
  
  
  
class DemographicsAdmin(ImportExportModelAdmin):
  list_display = ['question_part_one', 'question_part_one_tagalog']
  search_fields = ['question_part_one', 'question_part_one_tagalog']
  import_id_fields = ('question_part_one', 'question_part_one_tagalog')

  list_per_page = 15
  list_max_show_all = 50

class DemographicTwoAdmin(ImportExportModelAdmin):
  list_display = ['question_part_two', 'question_part_two_tagalog']
  search_fields = ['question_part_two', 'question_part_two_tagalog']
  import_id_fields = ('question_part_two', 'question_part_two_tagalog')

  list_per_page = 15
  list_max_show_all = 50


class PlayerAdmin(ImportExportModelAdmin):
    list_filter = ['gender', 'section', 'group', 'is_pending']
    list_display = ['username', 'surname','gender','section','group','age','is_pending','player_mode','date', 'is_complete_assessment']
    readonly_fields = ['player_mode','demographics', 'personality_test', 'game_scores', 'game_answer_history', 'user_session', 'uuid','pre_test_answer','pre_test_score', 'date', 'total_questions', 'correct_answers', 'wrong_answers', 'speed']

    fieldsets = (
        ('Personal Information',{
            'fields': (('username','surname'), ('group', 'is_pending'), 'age','gender','section','player_mode', 'date'),
        }),
        ('Assessments',{
            'fields': ('demographics', 'personality_test','pre_test_answer','pre_test_score','is_complete_assessment'),
        }),
        ('Game Results',{
            'fields': ('total_questions', 'speed', 'correct_answers', 'wrong_answers','game_answer_history'),
        }),
        ('Security ID',{
            'fields': ('user_session', 'uuid'),
        }),
    )
    search_fields = ['username','section']
    
admin.site.register(ResearchStatus, ResearchAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(PreTest, PreTestAdmin)
admin.site.register(PersonalityTest, PersonalityTestAdmin)
admin.site.register(DemographicsModel, DemographicsAdmin)
admin.site.register(DemographicsTwoModel, DemographicTwoAdmin)
