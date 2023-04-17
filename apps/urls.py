from django.urls import path
from .views import *



# 
urlpatterns = [
    # admin functions 
    path('manage_access', manage_user, name='manage_access'),
    
    # questions 
    path('question1', question1, name='question1'),
]
