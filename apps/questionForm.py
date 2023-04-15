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
        fields = ['answer']
        exclude = ['user', 'question', 'date_answered']
        
class Question2Form(ModelForm):
    pass 