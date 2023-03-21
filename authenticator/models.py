from django.db import models

# Create your models here.


# register client on the platform - admin only
class RegisterClient(models.Model):
    client_name = models.CharField(max_length=30)
    client_location = models.CharField(max_length=50) 
    date_registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.client_name

# This will generate password for user - action by admin only
class GeneratedPassword(models.Model):
    pass  


# where password will be accessed 
class PassWordSafe(models.Model):
    usage_count = models.PositiveIntegerField()
    client = models.ForeignKey(RegisterClient, on_delete=models.CASCADE, related_name='client registered password')


