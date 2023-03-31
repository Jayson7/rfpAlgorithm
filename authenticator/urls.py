
from django.urls import path, include
from .views import *



urlpatterns = [
    path('', login_page, name='login'),
    path('complete_info', complete_user_info, name='user_info'),
    
]
