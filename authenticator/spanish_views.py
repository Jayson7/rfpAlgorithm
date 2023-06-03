from django.shortcuts import render, redirect
from .auth_forms import *
from .models import *
from apps.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django_user_agents.utils import get_user_agent

import string
import random
import secrets
import datetime
from django.views.decorators.csrf import csrf_exempt




# check if all details are complete during taking of assessments 
def details_checker_questions_spanish(request):
    try:
        x = ['details', 'token_ses', 'browser', 'app_password']
   
        # filter to check if x data exists
        
        for i in x:
            if i in request.session:
                pass 
            else:
                return redirect('spanish_login')
    except:
        messages.warning(request, 'Perfil no documentado, acceso')
        return redirect('spanish_login')    
    
    

def basic_user_auth_check_spanish(request):
    if request.user.is_authenticated:
        pass  
    else:
        messages.warning(request, 'se necesita autenticación')
        return redirect('spanish_login')


# auth check admin
def basic_user_auth_check_admin_spanish(request):
    if request.user.is_superuser:
        pass  
    else:
        messages.warning(request, 'se necesita autenticación')
        return redirect('admin_login')





# ==================================== Basic functions and Algorithms =========================
# login here 

@csrf_exempt
def login_page_spanish(request):

#   set session expiry 
    request.session.set_expiry(0)
     
   
    context = {}
    if request.user.is_authenticated:
        # cleanup any leftover from user profile
        
        try:
            request.session.flush()
            logout(request)
   
        except:
            logout(request)
            
    else:
        pass 
    if request.method == "POST":
    
        password = request.POST['password1']
        full_name = request.POST['fullname']
   
        
        browser_prop = request.user_agent.browser 
        device = request.user_agent.device 
  

        # validate credentials
        if password == '' or full_name == '':
            messages.warning(request, 'credenciales incorrectas')
            return redirect('loginspanish')
        else:
            try:
                password_check = PasswordStorage.objects.get(password=password)
                if password_check:
                    # check password usage count 
                
                
                    if password_check.usage_count >= 1:
                        if password_check.usage_count == 1:
                            password_check.date_exhausted = datetime.datetime.now()
                            password_check.usage_count -= 1
                            
                            password_check.save()
                        else:
                        
                    
                            password_check.usage_count -= 1
                        
                            password_check.save()
                            
                           
                        
                        # get client details and authenticate
                        client_username = password_check.client.username
                    
                        
                        # i will use the auth password for authentication as auth password is different from app password that was acquired previously
                        
                        # locate auth_password
                        auth_password = RegisterClient.objects.get(username=client_username).auth_password
            
                        if client_username:
                            authenticate_user = authenticate(username=client_username, password=auth_password)
                            
                    
                            if authenticate_user is not None:
                                login(request, authenticate_user)
                                
                        
                                # create login token for user 
                                    # choose from all lowercase letter
                                letters = string.ascii_lowercase
                                result_str = ''.join(random.choice(letters) for i in range(4))
                                random_num = random.randint(1000, 9999)
                                token_generated = f'{result_str} + {random_num} + {result_str}'
                                
                              
                                              
                                # update session details for user                         #  
                                
                         
                       
                                request.session['token_ses'] = token_generated
                                request.session['auth_password'] = auth_password
                                request.session['app_password'] = password
                                request.session['user_profile'] = request.user.username
                                request.session['details'] = [browser_prop, device, full_name]
                                
                                
                                request.session['language'] = 'spanish'
                                print(request.session['language'] )
                                
                                # update session
                                request.session.modified = True
                                
                                return redirect('user_info_spanish')
                                
                            else:
                                messages.warning(request, 'La contraseña no es válida')
                                return redirect('loginspanish')
                                
                        else:
                            
                            messages.warning(request, 'Se deniega el acceso a la cuenta')
                            return redirect('loginspanish')
                            
                    else:
                        messages.warning(request, '¡Tu contraseña ha expirado!')
                        return redirect('loginspanish')
                    # if count limit isn't reached add 1 
                    
                    # generate token for user login using org username + count
                    
                    
                    # send user to info page
                    pass 
                else:
                    messages.warning(request, 'Contraseña incorrecta')
                    return redirect('loginspanish')
            except:
                messages.warning(request, 'Contraseña invalida')
                return redirect('loginspanish')        


    return render(request, 'auth_pages/user_login_spanish.html', context)





# complete user profile 
@csrf_exempt
def complete_user_info_spanish(request):
    # confirm authentication status    
    basic_user_auth_check_spanish(request)
    try:        
   
        if request.method == 'POST':
             if 'email' in request.session:
                 return redirect('question1s')
             
             else:
                email = request.POST['email']
                if email == '':
                    messages.warning(request, 'el correo electrónico no puede estar vacío')
                    return redirect('complete_info')
                
                else:
                    request.session['email'] = email 
                    
                    create_mom_data = Mom_data(
                        full_name= request.session['details'][2],    
                            app_password = request.session['app_password'], 
                    browser = request.session['details'][0],  
                    client_reference = request.user,
                    device_token =  request.session['token_ses'],
                    )
                    create_mom_data.save()
                    return redirect('question1s')
 
    except:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('login')
    return render(request, 'auth_pages/complete_profile_spanish.html')

