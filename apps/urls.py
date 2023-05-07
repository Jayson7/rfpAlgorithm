from django.urls import path
from .views import *



# 
urlpatterns = [
    # admin functions 
    path('manage_access', manage_user, name='manage_access'),
    path('details/<int:pk>', details, name='details'),
    
    # questions 
    path('question1', question1, name='question1'),
    path('question2', question2, name='question2'),
    path('question3', question3, name='question3'),
]
