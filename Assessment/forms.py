from django import forms
from django.forms import ModelForm
from .models import *
from revise_multiplayer.models import *

class PersonalityTestForm(ModelForm):
	class Meta:
		model = PersonalityTest
		fields = ['questions']

class DemographicForm(ModelForm):
	class Meta:
		model = Player
		fields = ['demographics']
    
class createAccountForm(ModelForm):
	class Meta:
		model = Player
		fields = ['username', 'surname', 'section', 'gender']




# username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control', 'id':'validationCustom01'}))
# email = forms.EmailField(max_length=50, help_text="Required. Add valid email address", label='Email : ',widget=forms.TextInput(attrs={'placeholder': 'Email', 'class':'form-control', 'id':'validationCustom03'}))
