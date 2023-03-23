from django.db import models

# Create your models here.

# take charge of usage of password by user 
class PasswordLog_on_User(models.Model):
    Full_name = models.CharField(max_length=40)
    age = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    email = models.EmailField()
    
    
    def __str__(self) -> str:
        return self.full_name


# register client on the platform - admin only
class RegisterClient(models.Model):
    client_name = models.CharField(max_length=30)
    client_location = models.CharField(max_length=50) 
    date_registered = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    
    
    

    
    def __str__(self) -> str:
        return self.client_name


# This will generate password for user - action by admin only

class GeneratedPassword(models.Model):
    client = models.ForeignKey(RegisterClient, on_delete=models.CASCADE)  
    usage_count = models.IntegerField()
    username = models.ForeignKey(RegisterClient, on_delete=models.CASCADE, related_name='org_username')
    
    
    def __str__(self) -> str:
        return self.client

# where password will be accessed by api only
class PassWordSafe(models.Model):
    usage_count = models.PositiveIntegerField()
    client = models.ForeignKey(RegisterClient, on_delete=models.CASCADE, related_name='client_registered_password')
    password = models.ForeignKey(GeneratedPassword, on_delete=models.CASCADE, related_name='password_saved')
    
    
    def __str__(self) -> str:
        return self.client

    



