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
    user_diagnosed = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='user_disease')
    points = models.IntegerField(default=0) 

    
    def __str__(self) -> str:
        return self.user_diagnosed
    

class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_to_ask')
    answer = models.CharField(max_length=200, null=True)
    user_print = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='user_in_question')

    
    def __str__(self) -> str:
        return self.user_print


# keep record of results by moms (all records) 
class ResultOfTest(models.Model):
    pass 
    



#  ========================================== All questions model =============


class Question1Model(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_storage')
    mom = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='questioned_user' )
    date_answered = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    token = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='token_questioned_user' )
    username_used = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='token_owner' )
    
    
    def __str__(self):
        return self.user