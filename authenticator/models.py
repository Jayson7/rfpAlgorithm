from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# =========================================================================

# register client on the platform - admin only

class RegisterClient(models.Model):
    client_name = models.CharField(max_length=30)
    client_location = models.CharField(max_length=50) 
    email = models.EmailField()
                            
    # auto generated
    date_registered = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20)
    
    
    def __str__(self) -> str:
        return self.client_name


# =========================================================================



# This will generate password for client  - action by admin only
class PasswordStorage(models.Model):
    
    client = models.ForeignKey(RegisterClient, on_delete=models.CASCADE, related_name='password_owner')
    password = models.CharField(max_length=12)
    date_generated = models.DateTimeField(auto_now_add=True)
    
    # hidden, will only be populated if password expires
    date_exhausted = models.DateTimeField(blank=True, null=True)
    usage_count = models.PositiveIntegerField(default=0)
    
    
    def __str__(self) -> str:
        return str(self.client)



# =========================================================================
# take charge of usage of password by user 
# when a user uses the password


class Password_log_on_user(models.Model):
    # height = models.FloatField(help_text='in meters, e.g 1.67')
    # weight = models.FloatField(help_text='in kilograms e.g 90kg')
    email = models.EmailField(help_text='abc@efg.com')
    # date_of_birth = models.DateField()
    
    # hidden, will be populated by api
    full_name = models.CharField(max_length=40)
    # BMI = models.FloatField(blank=True )
    password = models.ForeignKey(PasswordStorage, on_delete=models.CASCADE, related_name='password_patient_used')
    # age = models.PositiveIntegerField( blank=True)
    # classification = models.CharField(max_length=30)

    
    def __str__(self) -> str:
        return self.full_name
    

# ============================================================================
class UserLoginToken(models.Model):
    token = models.CharField(max_length=10)
    password = models.ForeignKey(PasswordStorage, on_delete=models.CASCADE, related_name='password_used_login')
    full_name =  models.CharField(max_length=30)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sign_on_user')
    verified = models.BooleanField(default=False)
    date_verified = models.DateTimeField(blank=True )
    date_token_generated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.full_name 