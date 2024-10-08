from django.db import models



# Create your models here.


# questions model

class Questions(models.Model):
    question = models.CharField(max_length=200) 
    id = models.AutoField(primary_key=True)
    

    def __str__(self) -> str:
        return self.question
    # questions model

class QuestionsSpanish(models.Model):
    question = models.CharField(max_length=200) 
    id = models.AutoField(primary_key=True)
    

    def __str__(self) -> str:
        return self.question
    
    
class Disease(models.Model):
    disease = models.CharField(max_length=100)
    user_diagnosed =  models.CharField(max_length=100)
    points = models.IntegerField(default=0) 
    id = models.AutoField(primary_key=True)
    
    
    def __str__(self) -> str:
        return str(self.user_diagnosed)  + '-' + str(self.disease) + '-' + str(self.points)   
    


class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='question_to_ask')
    answer = models.CharField(max_length=200, null=True)
    id = models.AutoField(primary_key=True)
    
    
    def __str__(self) -> str:
        return str(self.answer)


class AnswerSpanish(models.Model):
    question = models.ForeignKey(QuestionsSpanish, on_delete=models.CASCADE, related_name='question_to_ask_spanish')
    answer = models.CharField(max_length=200, null=True)
    id = models.AutoField(primary_key=True)
    
    
    def __str__(self) -> str:
        return str(self.answer)
    
    
class Referal(models.Model):
    token = models.CharField(max_length=30)
    patient = models.CharField(max_length=40)
    answer = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    
    
    
    def __str__(self) -> str:
        return str(self.patient)


#  ========================================== All questions model ============================



class Mom_data(models.Model):
    full_name = models.CharField(max_length=100)
    browser = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    app_password = models.CharField(max_length=100)
    client_reference = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    
    
    def __str__(self):
        return str(self.full_name)
    
    
    
class Disease_result(models.Model):
    disease = models.CharField(max_length=30)
    point = models.CharField(max_length=20)
    mom_full_name = models.CharField(max_length=20)
    date_generated = models.DateTimeField(auto_now_add=True)

    token = models.CharField(max_length=20, null=True)
    id = models.AutoField(primary_key=True)
    
    @property
    def id_alias(self):
        return self._id

    
    def __str__(self):
        return f"Disease_result {self.id}"
  
    
class Result_owner(models.Model):
    # disease_result = models.ForeignKey(Disease_result, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    token = models.CharField(max_length=20)
    auth_password = models.CharField(max_length=20)
    app_password = models.CharField(max_length=20)
    browser = models.CharField(max_length=100)

    user_profile = models.CharField(max_length=20)
    
    email = models.EmailField()
    age = models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)
   
        
    def __str__(self):
        return self.full_name    
  

class BMI(models.Model):
    bmi = models.CharField(max_length=30)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    token = models.CharField(max_length=30)
    full_name = models.CharField(max_length=40)
    id = models.AutoField(primary_key=True, null = False)
    
    def __str__(self):
        return str(self.token)
    
    
class ContactSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
    
    class SaveAnwersTemporarily(models.Model):
        pass 
    

