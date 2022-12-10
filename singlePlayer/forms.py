from django import forms

class SettingsForm(forms.Form):
  arithmetic = forms.CharField(label='arithmetic', max_length=100)
  difficulty = forms.CharField(label='difficulty', max_length=100)
  speed = forms.CharField(label='speed', max_length=100)
  lvl = forms.CharField(label='lvl', max_length=100)
