from django.forms import ModelForm
from .models import *
from django import forms



'''
Each question are configured based on the nature of such question

'''

# question 1
class Question1Form(ModelForm):
    class Meta:
        model = Question1Model
        fields = ['age']
        exclude = ['mom', 'question', 'date_answered', 'username_used', 'token']
        
class Question2Form(ModelForm):
   class Meta:
        model = Question2Model
        fields = ['height', 'weight']
        exclude = ['token', 'BMI']
