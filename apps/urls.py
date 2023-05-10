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
    path('question4', question4, name='question4'),
    path('question5', question5, name='question5'),
    path('question6', question6, name='question6'),
    path('question7', question7, name='question7'),
    path('question8', question8, name='question8'),
    path('question9', question9, name='question9'),
    path('question10', question10, name='question10'),
    path('question$', questionCombined, name='question$'),
    path('question15', question15, name='question15'),
    path('question16', question16, name='question16'),
]
