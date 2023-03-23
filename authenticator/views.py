from django.shortcuts import render, redirect
from .auth_forms import *
from .models import *
from django.contrib import messages
# Create your views here.



# login here 
def login_page(request):
    context = {}
    
    if request.method == "POST":
        forms = RegisterClientForm(request.POST)
        password = request.POST.get['password']
        print(password)
        if password == '':
            messages.warning(request, 'Password incorrect')
            return redirect('login')
        else:
            password_check = PassWordSafe.objects.filter(password=password)[0]
            if password_check.exists():
                pass 
            else:
                messages.warning(request, 'password incorrect')
                return redirect('login')
                
    return render(request, 'auth_pages/user_login.html', context)

def register_client(request):
    context = {}
    pass


# register mail here
def register_mail(request):
    pass

