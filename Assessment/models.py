from ast import operator
from email.policy import default
from django.db import models

from revise_multiplayer.models import *
# Create your models here.
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

OPERATOR_CHOICES = (
        ('+', 'Addition'),
        ('-', 'Subtraction'),
        ('×', 'Multiplication'),
        ('÷', 'Division'),
    )    

class ResearchStatus(models.Model):
    research_mode = models.BooleanField(default=True, verbose_name="Research Mode")

    @classmethod
    def object(cls):
        
        return cls._default_manager.all().first() # Since only one item

    def save(self, *args, **kwargs):
        self.pk = self.id = 1
        return super().save(*args, **kwargs)

    class Meta:
      verbose_name = "Research Mode"
      verbose_name_plural = "Research Mode"

    def __str_(self):
      return self.research_mode

class PersonalityTest(models.Model):
  id = models.AutoField(primary_key=True, verbose_name='Pre Assess ID')
  questions = models.CharField(max_length = 350, verbose_name='Questions')

  class Meta:
      verbose_name = "Personality Test"
      verbose_name_plural = "Personality Test"
  
  def __str_(self):
      return self.questions

class DemographicsModel(models.Model):
  question_part_one = models.CharField(max_length = 350, verbose_name='Questions I',blank=True, null=True,)
  question_part_one_tagalog = models.CharField(max_length = 350, verbose_name='Tagalog', blank=True, null=True,)
  
  class Meta:
      verbose_name = "Demographics Question I"
      verbose_name_plural = "Demographics Question I"

  def __str_(self):
      return self.question_part_one

class DemographicsTwoModel(models.Model):
  question_part_two = models.CharField(max_length = 350, verbose_name='Questions II',blank=True, null=True,)
  question_part_two_tagalog = models.CharField(max_length = 350, verbose_name='Tagalog', blank=True, null=True,)
  
  class Meta:
      verbose_name = "Demographics Question II"
      verbose_name_plural = "Demographics Question II"

  def __str_(self):
      return self.question_part_two


class PreTest(models.Model):
  operator = models.CharField(max_length = 50, choices=OPERATOR_CHOICES, verbose_name='Arithmetic Operators')
  q1 = models.CharField(max_length = 50, verbose_name='q1')
  q11 = models.CharField(max_length = 50, verbose_name='Optional', default=None, null=True, blank=True)

  q2 = models.CharField(max_length = 50, verbose_name='q2')
  q22 = models.CharField(max_length = 50, verbose_name='Optional', default=None, null=True, blank=True,)

  answer = models.CharField(max_length = 50, verbose_name='answer')

  def __str_(self):
      return self.q1

  class Meta:
      verbose_name = "Pre Test Question"



class Player(models.Model):
  uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

  username = models.CharField(max_length=250, verbose_name='Username', primary_key=True, unique=True)
  surname = models.CharField(max_length=250, verbose_name='Surname')
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
  age = models.PositiveIntegerField(verbose_name='Age')

  section = models.CharField(max_length=250, verbose_name='Section', blank=True, null=True)

  group =  models.ForeignKey(Group, on_delete=models.PROTECT, default=None, null=True, blank=True, help_text="Add Group for your student")
  user_session = models.CharField(max_length=150,verbose_name='User Session', null=True)
  # In-game fields 
  demographics =  models.TextField(verbose_name='Demographics', blank=True)
  personality_test =  models.TextField(verbose_name='Personality Test', blank=True)
  pre_test_answer = models.TextField(verbose_name='Pre-Test Answers', blank=True)
  pre_test_score = models.TextField(max_length=150,verbose_name='Pre-test Score', blank=True)
  is_complete_assessment = models.BooleanField(default=False)

  game_scores = models.TextField(verbose_name='Game Scores', blank=True)
  game_answer_history = models.TextField( verbose_name='Game Answers', blank=True)

  speed = models.CharField(max_length=250, verbose_name='Speed', null=True, blank=True)
  total_questions = models.CharField(max_length=250, verbose_name='Total Questions', null=True, blank=True)
  correct_answers = models.CharField(max_length=250, verbose_name='Correct Answers', null=True, blank=True)
  wrong_answers = models.CharField(max_length=250, verbose_name='Wrong Answers', null=True, blank=True)


  player_mode = models.CharField(max_length=250, verbose_name='Player Mode', null=True, blank=True)
  is_pending = models.BooleanField(default=True, verbose_name="Pending")

  date = models.DateField(auto_now_add=False, null=True)

  
  def __str__(self):
      return  self.username

  def clean(self):
      self.username = self.username.capitalize()
      self.surname = self.surname.capitalize()