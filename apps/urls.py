from django.urls import path
from .views import *



# 
urlpatterns = [
    path('question1', question1, name='question1'),
]
