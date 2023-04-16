from django.urls import path
from .views import *



# 
urlpatterns = [
    # admin functions 
    path('manage_user', manage_user, name='manage_user'),
    
    # questions 
    path('question1', question1, name='question1'),
]
