from django.forms import ModelForm
from .models import *


class ResgisterUser(ModelForm):

    class Meta:
        model = RegisterClient
        fields = ['usage_permission_count', 'client_name',
                  'client_location'
                  ]
        
