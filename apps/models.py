from django.db import models



# Create your models here.


# questions model

class Questions(models.Model):
    question = models.CharField(max_length=200) 


    def __str__(self) -> str:
        return self.question
    
    
class Disease(models.Model):
    disease = models.CharField(max_length=100)
    user_diagnosed =  models.CharField(max_length=200)
    points = models.FloatField() 

    
    def __str__(self) -> str:
        return str(self.user_diagnosed)  + '-' + str(self.disease) + '-' + str(self.points)   
    


class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_to_ask')
    answer = models.CharField(max_length=200, null=True)

    
    def __str__(self) -> str:
        return str(self.answer)




#  ========================================== All questions model ============================



class Mom_data(models.Model):
    full_name = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    device_token = models.CharField(max_length=100)
    app_password = models.CharField(max_length=100)
    client_reference = models.CharField(max_length=100)
    
    
    def __str__(self):
        return str(self.full_name)
    
    
    

    
  