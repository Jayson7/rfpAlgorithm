from django.db import models

# Create your models here.



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




# monitor password usage for api
class PasswordStorage(models.Model):
    client = models.ForeignKey(RegisterClient, on_delete=models.CASCADE, related_name='password_owner')
    password = models.CharField(max_length=12)
    date_generated = models.DateTimeField(auto_now_add=True)
    
    # hidden, will only be populated if password expires
    date_exhausted = models.DateTimeField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.client



# count password access 
class Usage_Monitor(models.Model):
    client = models.ForeignKey(RegisterClient, on_delete=models.CASCADE, related_name='password_used_owner')
    usage_count = models.PositiveIntegerField(default=0)
    password = models.ForeignKey(PasswordStorage, on_delete=models.CASCADE, related_name='password_involved')
     



# This will generate password for user - action by admin only

class GeneratedPassword(models.Model):
    client = models.ForeignKey(RegisterClient, on_delete=models.CASCADE)  
    usage_count = models.ForeignKey(Usage_Monitor,on_delete=models.CASCADE, related_name='password_count')
    # auto generated
    password = models.ForeignKey(PasswordStorage, on_delete=models.CASCADE, related_name='password_expected')
    
    
    def __str__(self) -> str:
        return self.client



# take charge of usage of password by user 
# when a user uses the password

class Password_log_on_user(models.Model):
    full_name = models.CharField(max_length=40)
    
    height = models.FloatField()
    weight = models.FloatField()
    email = models.EmailField()
    date_of_birth = models.DateField()
    
    # hidden, will be populated by api
    
    password = models.ForeignKey(PasswordStorage, on_delete=models.CASCADE, related_name='password_patient_used')
    
    
    
    def __str__(self) -> str:
        return self.full_name
    
    
class UserLoginToken(models.Model):
    token = models.CharField(max_length=10)
    password = models.ForeignKey(PasswordStorage, on_delete=models.CASCADE, related_name='password_used_login')
    full_name =  models.CharField(max_length=30)
    
    
    def __str__(self) -> str:
        return self.token 