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
    auth_password = models.CharField(max_length=15)
    id = models.AutoField(primary_key=True)
    
    
    
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
    id = models.AutoField(primary_key=True)
    
    
    def __str__(self) -> str:
        return str(self.password)






# _____________________________________________________________________
# ============================================================================




    
    
    
    
    
    
    
    
    
    