from django.forms import ModelForm
from .models import *


class RegisterClientForm(ModelForm):

    class Meta:
        model = RegisterClient
        fields = [ 'client_name',
                  'client_location'
        ]
        

class CompeteProfileForm(ModelForm):
    
    class Meta:
        model = Password_log_on_user
        fields = [
            'age', 'height', 'weight', 'email', 'date_of_birth' 
        ]
        exclude = ['full_name', 'password']
        

