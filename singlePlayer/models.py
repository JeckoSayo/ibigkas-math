from tabnanny import verbose
from django.db import models
from Assessment.models import *
# Create your models here.

class GameSetting(models.Model):
  setting_id = models.BigAutoField(primary_key=True, verbose_name="ID")
  player = models.ForeignKey(Player, on_delete=models.CASCADE, verbose_name="Player")
  arithmetic = models.CharField(max_length=250, verbose_name='Arithmetic')
  difficulty = models.CharField(max_length=250, verbose_name='Difficulty')
  speed = models.CharField(max_length=250, verbose_name='Speed')
  lvl = models.CharField(max_length=250, verbose_name='lvl')

