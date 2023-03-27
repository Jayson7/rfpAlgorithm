from django.shortcuts import render, redirect
from .auth_forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.



# login here 
def login_page(request):
    context = {}
    
    if request.method == "POST":
    
        password = request.POST['password1']
       
        if password == '':
            messages.warning(request, 'Password incorrect')
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
                            pass
                         
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




# update models for password count on login

def UpdatePassword(request):
    pass



# generate a new password for new client
def generate_password_new_user(request):
    pass 



# generate a new password for existing client
def generate_password_old_user(request):
    pass 

