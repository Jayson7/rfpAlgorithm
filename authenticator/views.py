from django.shortcuts import render, redirect
from .auth_forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

import string
import random
import secrets
import datetime


# Create your views here.

# helper functions 


# super user checker
def super_user_check(request):
    if request.user.is_superuser:
        pass 
    else:
        messages.warning(request, 'That wont work')
        return redirect('login')


# auth check normal user
def basic_user_auth_check(request):
    if request.user.is_authenticated:
        pass  
    else:
        messages.warning(request, 'authentication needed')
        return redirect('login')


# auth check admin
def basic_user_auth_check_admin(request):
    if request.user.is_authenticated:
        pass  
    else:
        messages.warning(request, 'authentication needed')
        return redirect('admin_login')



# ==================================== Basic functions and Algorithms =========================
# login here 
def login_page(request):
    
    
    
    context = {}
    if request.user.is_authenticated:
        # cleanup any leftover from user profile
        try:
            access_token = UserLoginToken.objects.filter(username = request.user).token.first()
            if access_token:
                access_token.delete() 
                logout(request)
            else:
                logout(request)
        except:
            logout(request)
            
    else:
        pass 
    if request.method == "POST":
    
        password = request.POST['password1']
        full_name = request.POST['fullname']
        # validate credentials
        if password == '' or full_name == '':
            messages.warning(request, 'Incorrect credentials')
            return redirect('login')
        else:
            password_check = PasswordStorage.objects.filter(password=password).first()
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
                            auth_password_owner = RegisterClient.objects.get(username=request.user)
                          
                    
                            # create login token for user 
                                # choose from all lowercase letter
                            letters = string.ascii_lowercase
                            result_str = ''.join(random.choice(letters) for i in range(4))
                            random_num = random.randint(1000, 9999)
                            token_generated = f'{result_str} + {random_num} + {result_str}'
                            print(token_generated)
                            
                            token_create = UserLoginToken(
                                 token = token_generated,
                                 password = password_check,
                                 full_name = full_name,
                                 username = auth_password_owner
                             )
                            
                            token_create.save()
                            
                            
                            return redirect('user_info')
                            
                        else:
                            messages.warning(request, 'Password is invalid')
                            return redirect('login')
                            
                    else:
                        
                        messages.warning(request, 'Account access is denied, contact Admin')
                        return redirect('login')
                        
                else:
                    messages.warning(request, 'Your password has expired!')
                    return redirect('login')
                # if count limit isn't reached add 1 
                
                # generate token for user login using org username + count
                
                
                # send user to info page
                pass 
            else:
                messages.warning(request, 'Incorrect Password')
                
                print('lost')
                return redirect('login')

    return render(request, 'auth_pages/user_login.html', context)




# complete user profile 

def complete_user_info(request):
    
    # confirm authentication status    
    if request.user.is_authenticated:
       
        pass 
    else:
   
        return redirect('login')
    
    try:
        
        print(request.user, 'email')
        registered_client_profile = RegisterClient.objects.filter(username = request.user).first()
        print(registered_client_profile, 'access owner')
        access_token = UserLoginToken.objects.get(username=registered_client_profile)
        
        # verify token
        if access_token:
            pass  
        else:
            messages.warning(request, 'Access not authorized')
            return redirect('login')
        
        
    except:
        messages.warning(request, 'Authentication failed')
        return redirect('login')
    

    context = {}
    if access_token:
        forms = CompeteProfileForm(request.POST, request.FILES)
        if request.method == 'POST':
            
            if forms.is_valid():
              
                
                # load full name and password
                full_name = access_token.full_name 
                password = access_token.password
                #  trigger other left out details
                forms.full_name = full_name
                forms.password = password

        
                forms.save()
                # verify user by adding verification to token
                access_token.verified = True 
                access_token.save()
                
                # start questions 
                return redirect('question_controller')
                
            else:
                forms = CompeteProfileForm()
                messages.warning(request, 'Invalid input')
        else:
            forms = CompeteProfileForm()
            messages.success(request, 'One more thing')
            
    
    context['forms'] = forms
    
    return render(request, 'auth_pages/complete_profile.html', context)



# ========================================= Admin functions ===================================================

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
                        return redirect('login')
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
            all_moms_login_data = Password_log_on_user.objects.all()[::-1]
            context['moms_login'] = all_moms_login_data
            return render(request, 'admin_pages/admin_dashboard.html', context)      
        
        else:
            messages.warning(request, 'Trying to access that wont work')
            return redirect('login')
        
    else:
        messages.warning(request, 'Login please')
        return redirect('admin_login')



# update models for password count on login

def UpdatePassword(request):
    if request.user.is_authenticated:
        pass 
    else:
        return redirect('login')
    
    


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
                                        
                                        client = RegisterClient.objects.get(client_name=user_in_question.client_name)
                                       
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
                                client = RegisterClient.objects.get(client_name=user_in_question.client_name)
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
            return redirect('login')        
    
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
                    if name_check and email_check:
                      
                        messages.warning(request, 'user already exist')
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
    basic_user_auth_check_admin(request)
    super_user_check(request)    
 
    
    user = PasswordStorage.objects.get(id=pk)
    if user:
        user.usage_count = 0
        user.save()
        messages.success(request, 'Access removed')
        return redirect('manage_access')
    else:
        messages.warning(request, 'Account does not exist')
        return redirect('manage_access')
    
    return render(request, 'admin_pages/manage_user.html')


# re-generate password for old users
def regenerate_password(request, pk):
    basic_user_auth_check_admin(request)
    super_user_check(request)
    
    user = PasswordStorage.objects.get(id=pk)
    print(user)
    if user:
       
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
                           
        user.password = app_password
        user.save()         

     
                                    
        messages.success(request, 'Password updated successfully')
                                    
        return redirect('manage_access')
    

    else:
        messages.warning(request, 'Account does not exist')
        return redirect('manage_access')
    
    