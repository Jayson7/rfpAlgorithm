from django.forms import ModelForm
from .models import RegisterClient


class RegisterClientForm(ModelForm):

    class Meta:
        model = RegisterClient
        fields = [ 'client_name',
                  'client_location'
        ]
        

        
# class ResgisterUser(ModelForm):

#     class Meta:
#         model = RegisterClient
#         fields = ['usage_permission_count', 'client_name',
#                   'client_location'
#                   ]
        
