from django.db import models

# Create your models here.

class LoginPassword():
  
    pass

class RegisterClient(models.Model):
    usage_permission_count = models.IntegerField()
    client_name = models.CharField(max_length=30)
    client_location = models.CharField(max_length=50) 
    date_registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.client_name
   