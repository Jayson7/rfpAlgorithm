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
    

class Stopped_answering(models.Model):
    user = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='user_taking_questions')
    current_stop = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='last_question')
    
class Unanswered_questions(models.Model):
    all_questions = models.ManyToManyField(Questions, related_name='all_unanswered_questions') 
    user = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='the_user')
    
class Answered_questions(models.Model):
    questions = models.ManyToManyField(Questions, related_name='all_answered_questions') 
    user = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='the_user_answered')
    
    

#  ========================================== All questions model =============


class Question1Model(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_storage')
    user = models.ForeignKey(UserLoginToken, on_delete=models.CASCADE, related_name='questioned_user' )
    date_answered = models.DateTimeField(auto_now_add=True)
    answer = models.IntegerField()
    
    def __str__(self):
        return self.user