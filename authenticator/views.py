from django.shortcuts import render, redirect
from .auth_forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import string
import random

# Create your views here.


# ==================================== Basic functions and Algorithms =========================
# login here 
def login_page(request):
    context = {}
    if request.user.is_authenticated:
        # cleanup any leftover from user profile
        
        logout()
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
                usage_count_password = Usage_Monitor.objects.filter(password=password_check).usage_count
                print(usage_count_password)
                if usage_count_password >= 1:
                    usage_count_password - 1
                    usage_count_password.save()
                    # get client details and authenticate
                    client_username = password_check.client.username 
                    if client_username:
                        authenticate_user = authenticate(client_username, password)
                        if authenticate_user.is_authenticated:
                            
                            # create login token for user 
                                # choose from all lowercase letter
                            letters = string.ascii_lowercase
                            result_str = ''.join(random.choice(letters) for i in range(4))
                            random_num = random.randint(1000, 9999)
                            token_generated = f'{result_str} + {random_num} + {result_str}'
                            print(token_generated)
                            
                            token_create = UserLoginToken.create(
                                 token = token_generated,
                                 password = password_check,
                                 full_name = full_name,
                                 username = client_username
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
    # if request.user.is_authenticated:
    #     pass 
    # else:
    #     return redirect('login')
    
    # try:
    #     access_token = UserLoginToken.objects.filter(username = request.user).token.first()
    # except:
    #     messages.warning(request, 'Authentication failed')
    #     return redirect('login')
    
    # access_token = True 
    current_user = request.user
    context = {}
    forms = CompeteProfileForm()
    if request.method == 'POST':
        pass 
        if forms.is_valid():
            new_profile = forms.save(commit=False)
            
            # load full name and password
            full_name = access_token.full_name 
            password = access_token.password
            #  trigger other left out details
            new_profile.full_name = full_name
            new_profile.password = password
            # calculate BMI
            print(new_profile.height)
            print(new_profile.weight)
            new_profile.BMI =float(new_profile.height) * float(new_profile.height) / float(new_profile. width)
            profile_score = float(new_profile.BMI)
            
            
            # define classification
            
            if profile_score < 18.5:
                new_profile.classification = 'Under Weight'
            elif profile_score  >= 18.5 and profile_score <= 24.9:
                new_profile.classification = 'normal'
            
            elif profile_score  >= 25 and profile_score <= 29.9:
                new_profile.classification = 'Over Weight'
            
            elif profile_score  >= 30 and profile_score <= 34.9:
                new_profile.classification = 'Obesity (Class I)'
            
            elif profile_score  >= 35 and profile_score <= 39.9:
                new_profile.classification = 'Obesity (Class II)'
            
            else:
                new_profile.classification = 'Extreme Obesity'
       
            new_profile.save()
            
            # submit and start questions

    else:
        forms = CompeteProfileForm()
    
    context['forms'] = forms
    
    return render(request, 'auth_pages/complete_profile.html', context)







# ========================================= Admin functions ===================================================


# update models for password count on login

@login_required
def UpdatePassword(request):
    pass


# generate a new password for new client
@login_required
def generate_password_new_user(request):
    pass


# generate a new password for existing client
@login_required
def generate_password_old_user(request):
    pass 

