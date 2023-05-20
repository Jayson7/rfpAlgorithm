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



            