from django.shortcuts import render, redirect
from .auth_forms import *
from .models import *
from django.contrib import messages
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
            password_check = GeneratedPassword.objects.filter(password=password).first()
            if password_check:
                # check password usage count 
                usage_count_password = PassWordSafe.objects.filter(password=password).usage_count
                if usage_count_password >= 1:
                    pass 
                else:
                    messages.warning(request, 'password is exhausted')
                    return redirect('login')
                # if count limit isn't reached add 1 
                
                # generate token for user login using org username + count
                
                
                # send user to info page
                pass 
            else:
                messages.warning(request, 'password incorrect')
                return redirect('login')

    return render(request, 'auth_pages/user_login.html', context)

def register_client(request):
    context = {}
    pass




