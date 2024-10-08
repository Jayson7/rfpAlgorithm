
from django.urls import path, include
from .views import *
from .spanish_views import *



urlpatterns = [
    # user functions 
    path('logins', login_page, name='logins'),
    path('complete_info', complete_user_info, name='user_info'),
    
    
    # spanish
    path('loginspanish', login_page_spanish, name='loginspanish'),
    path('complete_info_spanish', complete_user_info_spanish, name='user_info_spanish'),
    
    
    
    
    
    # admin functions
    path('admin_login', admin_login, name='admin_login'),
    path('admin_dashboard', admin_dashboard, name='admin_dashboard'),
    path('create_user', create_user, name='create_user'),
    path('generate_password/<int:pk>', generate_password, name='generate_password'),
    path('regenerate_password/<int:pk>', regenerate_password, name='regenerate_password'),
    path('remove_access/<int:pk>', removeAccess, name='remove_access'),

]




