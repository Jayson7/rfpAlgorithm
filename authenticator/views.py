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

# Create your views here.


# check if all details are complete during taking of assessments 
def details_checker_questions(request):
    try:
        x = ['details', 'token_ses', 'browser', 'app_password']
   
        # filter to check if x data exists
        
        for i in x:
            if i in request.session:
                pass 
            else:
                return redirect('logins')
    except:
        messages.warning(request, 'Profile undocumented, login')
        return redirect('logins')    

# check if all details are complete during taking of assessments 
def details_checker_questions_spanish(request):
    try:
        x = ['details', 'token_ses', 'browser', 'app_password']
   
        # filter to check if x data exists
        
        for i in x:
            if i in request.session:
                pass 
            else:
                return redirect('loginspanish')
    except:
        messages.warning(request, 'Perfil indocumentado, iniciar sesión')
        return redirect('loginspanish')    
# helper functions 

# auth check user
def basic_user_auth_check(request):
    if request.user.is_authenticated:
        pass  
    else:
        messages.warning(request, 'authentication needed')
        return redirect('logins')
    
# auth check user
def basic_user_auth_check_spanish(request):
    if request.user.is_authenticated:
        pass  
    else:
        messages.warning(request, 'autenticación necesaria')
        return redirect('loginspanish')


# auth check admin
def basic_user_auth_check_admin(request):
    if request.user.is_superuser:
        pass  
    else:
        messages.warning(request, 'authentication needed')
        return redirect('admin_login')



# ==================================== Basic functions and Algorithms =========================
# login here 

@csrf_exempt
def login_page(request):
   
    request.session.set_expiry(0)
   
    context = {}

   
    if request.user.is_authenticated:
        # cleanup any leftover from user profile
        
        try:
            request.session.flush()
            logout(request)
   
        except:
            logout(request)
            
    
    if request.method == "POST":
    
    
    
        password = request.POST['password1']
        full_name = request.POST['fullname']
   
        
        browser_prop = request.user_agent.browser 
        device = request.user_agent.device 
  
      
        
        # validate credentials
        if password == '' or full_name == '':
            messages.warning(request, 'Incorrect credentials')
            return redirect('logins')
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
                                
                                request.session['language'] = 'english'
                                print(request.session['language'] )

                                # update session
                                request.session.modified = True
                                
                                return redirect('user_info')
                                
                            else:
                                messages.warning(request, 'Password is invalid')
                                return redirect('logins')
                                
                        else:
                            
                            messages.warning(request, 'Account access is denied')
                            return redirect('logins')
                            
                    else:
                        messages.warning(request, 'Your password has expired!')
                        return redirect('logins')
                    # if count limit isn't reached add 1 
                    
                    # generate token for user login using org username + count
                    
                    
                    # send user to info page
                    pass 
                else:
                    messages.warning(request, 'Incorrect Password')
                    return redirect('logins')
            except:
                messages.warning(request, 'Invalid Password')
                return redirect('logins')        


    return render(request, 'auth_pages/user_login.html', context)


# complete user profile 
@csrf_exempt
def complete_user_info(request):
    # confirm authentication status    
    basic_user_auth_check(request)
  
   
            
    if request.method == 'POST':
            if 'email' in request.session:
                return redirect('question1')
             
            else:
                email = request.POST['email']
                if email == '':
                    messages.warning(request, 'email cannot be empty')
                    return redirect('complete_info')
                
                else:
                    request.session['email'] = email 
                    
                    create_mom_data = Mom_data(
                        full_name= request.session['details'][2],    
                            app_password = request.session['app_password'], 
                    browser = request.session['details'][0],  
                    client_reference = request.user,
                 
                    )
                    create_mom_data.save()
                    return redirect('question1')
 
  
    return render(request, 'auth_pages/complete_profile.html')


# ========================================= Admin functions ===================================================
@csrf_exempt
def admin_login(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        pass 
    
    context = {}
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 
        # verify credentials 
        
        try:
            verified_username = User.objects.filter(username=username).first()
            print(verified_username)
           
            if verified_username:
                user = authenticate(username=username, password=password)  
                if user.is_active:
                    # check superuser status 
                    if user.is_superuser:
                        login(request, user)
                        return redirect('admin_dashboard')
                    else:
                        logout(request, user)
                        messages.warning(request, 'Trying to access that wont work')
                        return redirect('logins')
                else:
                    messages.warning(request, 'Wrong username and password')
                    return redirect('admin_login')
            else:
                messages.warning(request, 'Username incorrect')
                return redirect('admin_login')
                
        except:
            messages.warning(request, 'authentication failed')
            return redirect('admin_login')
    else:
        pass 
    
    return render(request, 'admin_pages/admin_login.html', context)
 


def admin_dashboard(request):
    context = {}
    # check login status

    if request.user.is_authenticated:
        # check super user status 
        if request.user.is_superuser:
            all_moms_login_data = Result_owner.objects.all()[::-1]
            context['moms_login'] = all_moms_login_data
            
            # segmented data
            
            context['total_patient'] = Result_owner.objects.count()
            context['test_taken'] = Result_owner.objects.count()
            context['hospital'] = RegisterClient.objects.count()
            context['access'] = PasswordStorage.objects.count()
            
        
        else:
            messages.warning(request, 'Trying to access that wont work')
            return redirect('logins')
        
    else:
        messages.warning(request, 'Login please')
        return redirect('admin_login')
    
    return render(request, 'admin_pages/admin_dashboard.html', context)      




# update models for password count on login

def UpdatePassword(request):
    if request.user.is_authenticated:
        pass 
    else:
        return redirect('logins')
    
 
# generate a new password for new client


def generate_password(request, pk):
    context={}
    if request.user.is_authenticated:
        if request.user.is_superuser:
            try:
                user_in_question = RegisterClient.objects.filter(id=pk).first()
                context['client'] = user_in_question
                
                if user_in_question:
                    
                    if request.method =="POST":
                            count = request.POST['count']
                            if int(count) == 0:
                                messages.warning(request, 'A zero access count wont work')
                                return HttpResponseRedirect(request.path_info)
                            else:
                                
                                
                                # get previous count total
                                try:
                                    password_prev = PasswordStorage.objects.filter(client=user_in_question).first()
                                    
                                    if password_prev:
                                        print(password_prev.usage_count)
                                        prev_count = password_prev.usage_count 
                                        count = int(count) + int(prev_count)  
                                        # proceed
                                        
                                        client = RegisterClient.objects.get(username=user_in_question.username)
                                       
                                        password_prev.usage_count = count
                                         
                                        password_prev.save()
                                            
                                        messages.success(request, 'Access count modified successfully')
                                            
                                        return redirect('manage_access')  
                                    else:
                                        pass
                                except:
                                    pass
                                    # generate password for user 
                            
                                    # define the alphabet
                                client = RegisterClient.objects.get(username=user_in_question.username)
                                letters = string.ascii_letters
                                digits = string.digits
                                special_chars = string.punctuation

                                alphabet = letters + digits + special_chars

                                    # fix password length
                                pwd_length = 10

                                    # generate a password string
                                pwd = ''
                                for i in range(pwd_length):
                                    pwd += ''.join(secrets.choice(alphabet))

                                app_password = pwd
                                    
                                
                                created_password = PasswordStorage(
                                        client = client,
                                        password = app_password,
                                        usage_count = int(count),
                                        
                                    )
                                
                                created_password.save()
                                    
                                messages.success(request, 'Access updated successfully')
                                    
                                return redirect('manage_access')
                         
            except:
                messages.warning(request, 'No user found')
                return redirect('manage_access')
        else:
            messages.warning(request, 'You dont have that access')
            return redirect('logins')        
    
    else:
        return redirect('admin_login')
    
    return render(request, 'auth_pages/generatePassword.html', context)

# generate a new password for existing client

# admin function to create a user on the platform 

def create_user(request):
    context={}
    user = request.user 
    if user.is_authenticated:
        # confirm superuser status
        
        # segmented data
            
        context['total_patient'] = Result_owner.objects.count()
        context['test_taken'] = Result_owner.objects.count()
        context['hospital'] = RegisterClient.objects.count()
        context['access'] = PasswordStorage.objects.count()
            
        if user.is_superuser:
            
            if request.method == 'POST':
                
                name = request.POST['full_name']
                address = request.POST['address']
                email = request.POST['email']

                # verify credentials 

                # check name 

                try:
                    
                    name_check = RegisterClient.objects.filter(client_name=name).exists()
                    email_check = RegisterClient.objects.filter(email=email).exists()
                    print(email)
                    if name_check or email_check:
                      
                        messages.warning(request, 'user already profile exist ')
                        return redirect('create_user')
                    
                    else:
                        print('trying')
                        
                        # generate password
               
                        letters = string.ascii_letters
                        digits = string.digits
                        special_chars = string.punctuation

                        alphabet = letters + digits + special_chars

                        # fix password length
                        pwd_length = 15

                        # generate a password string
                        pwd = ''
                        for i in range(pwd_length):
                            pwd += ''.join(secrets.choice(alphabet))

                        app_password = pwd
                        
                        
                        # generate username
                        user_generated_username = f"{name.replace(' ', '')}{random.randint(1,100)}"
                       
                        # create auth profile 
                        reg_user=User.objects.create_user(
                            
                            username= user_generated_username,
                            email=email,
                            password= app_password,
                            first_name = name,
                            last_name = name 
                        )
                        reg_user.save()
                        print('done')
                        
                        # create registry profile
                        
                        new_user= RegisterClient(
                            client_name = name, 
                            client_location = address,
                            email = email,
                            username = user_generated_username,
                            auth_password= app_password
                        )
                    
                        new_user.save()
                        messages.success(request, 'User created successfully')
                        
                        return redirect('manage_access')
                except:
                    
                    messages.warning(request, 'Error occurred while verifying credentials')
                    return redirect('create_user')
    
    else:
        return redirect('admin_login')
    return render(request, 'auth_pages/create_profile.html', context)



def removeAccess(request, pk):
    # locate the primary key on password storage 
    try:
        user = PasswordStorage.objects.get(id=pk)
    except:
       user =  None
    if user:
        user.usage_count = 0
        user.save()
        messages.success(request, 'Access removed')
        return redirect('manage_access')
    else:
        messages.warning(request, 'Access does not exist')
        return redirect('manage_access')
    

# re-generate password for old users

def regenerate_password(request, pk):
    basic_user_auth_check_admin(request)
    try:
        user = RegisterClient.objects.get(id=pk)
        find_pass_profile = PasswordStorage.objects.get(client=user)
    except:
        messages.warning(request, 'Cant locate user password account')
        return redirect('manage_access')
    
    print(find_pass_profile)
    if find_pass_profile:
       
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        alphabet = letters + digits + special_chars

                                    # fix password length
        pwd_length = 10

                                    # generate a password string
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        app_password = pwd
                           
        find_pass_profile.password = app_password
        find_pass_profile.save()         

     
                                    
        messages.success(request, 'Password updated successfully')
                                    
        return redirect('manage_access')
    

    else:
        messages.warning(request, 'Account does not exist')
        return redirect('manage_access')
    
    

# deactivate authentication 

def deactivate_auth(request):
    if request.user.is_authenticated:
        logout(request)
        
    else:
        pass 
    