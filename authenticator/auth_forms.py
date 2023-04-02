from django.forms import ModelForm
from .models import *
from django import forms

class RegisterClientForm(ModelForm):

    class Meta:
        model = RegisterClient
        fields = [ 'client_name',
                  'client_location'
        ]
        

class DateInput(forms.DateInput):
    input_type = 'date'

# Form class in forms.py


class CompeteProfileForm(forms.ModelForm):
    
    date_of_birth = forms.DateField(widget=DateInput)
    
    class Meta:
        model = Password_log_on_user
        fields = [
             'height', 'weight', 'email', 'date_of_birth' 
        ]
        exclude = ['full_name', 'password', 'BMI', 'age']
        

