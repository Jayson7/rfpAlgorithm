
from django.urls import path, include
from .views import *



urlpatterns = [
    # user functions 
    path('', login_page, name='login'),
    path('complete_info', complete_user_info, name='user_info'),
    
    # admin functions
    path('admin_login', admin_login, name='admin_login'),
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),
    path('create_user', create_user, name='create_user'),
    path('generate_password/<int:pk>', generate_password, name='generate_password'),
    path('regenerate_password/<int:pk>', regenerate_password, name='regenerate_password'),
    path('remove_access/<int:pk>', removeAccess, name='remove_access'),
    path('uncheck', uncheck, name='uncheck'),

]




