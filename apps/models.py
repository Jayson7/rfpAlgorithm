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
        return str(self.user_diagnosed)
    

class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_to_ask')
    answer = models.CharField(max_length=200, null=True)
    user_print = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='user_in_question', null=True, blank=True)
    verified = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return str(self.answer)




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
        return str(self.mom)
    
    
class Question2Model(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_storage_q2')
    date_answered = models.DateTimeField(auto_now_add=True)
    height = models.FloatField(help_text='in cms')
    weight = models.FloatField(help_text='in kgs')
    token = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='token_questioned_user_q2' )
    BMI = models.CharField(max_length=20)
    
    
    
    def __str__(self):
        return str(self.BMI)
    


    
  