from django.db import models
from authenticator.models import  UserLoginToken

# Create your models here.


# questions model

class Questions(models.Model):
    pass 

class Disease(models.Model):
    pass 


class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_to_ask')
    answer = models.CharField(max_length=200, null=True)
    user_print = models.ForeignKey()
