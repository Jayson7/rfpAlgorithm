from django.forms import ModelForm
from .models import *
from django import forms

class RegisterClientForm(ModelForm):

    class Meta:
        model = RegisterClient
        fields = [ 'client_name',
                  'client_location'
        ]
        

# class DateInput(forms.DateInput):
#     input_type = 'date'

# Form class in forms.py


class CompeteProfileForm(forms.ModelForm):
    
    # date_of_birth = forms.DateField(widget=DateInput)
    
    class Meta:
        model = Password_log_on_user
        fields = [
            'email'
        ]
        exclude = ['full_name', 'password']
        
class GeneratePAsswordForm(ModelForm):
    
    class Meta:
        
        model = PasswordStorage
        fields = ['usage_count']
        exclude = ['client','date_generated', 'date_exhausted','password' ]


