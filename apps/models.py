from django.db import models
from authenticator.models import  UserLoginToken


# Create your models here.


# questions model

class Questions(models.Model):
    question = models.CharField(max_length=200) 


    def __str__(self) -> str:
        return self.question
    
class Disease(models.Model):
    disease = models.CharField(max_length=100)
    user_diagonised = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='user_disease')
    points = models.IntegerField(default=0) 

    
    def __str__(self) -> str:
        return self.user_diagonised

class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_to_ask')
    answer = models.CharField(max_length=200, null=True)
    user_print = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='user_in_question')

    
    def __str__(self) -> str:
        return self.user_print
    
