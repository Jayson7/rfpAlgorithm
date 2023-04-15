
from django.urls import path, include
from .views import *



urlpatterns = [
    # user functions 
    path('', login_page, name='login'),
    path('complete_info', complete_user_info, name='user_info'),
    
    # admin functions
    path('admin_login', admin_login, name='admin_login'),
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),
  

]
