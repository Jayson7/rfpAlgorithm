from django.shortcuts import render, redirect
from .auth_forms import *
# Create your views here.



# login here 
def login_page(request):
    context = {}
    forms = RegisterClient()
    
    if request.method == "POST":
        pass
    
    
    return render(request, 'auth_pages/user_login.html', context)

def register_client(request):
    context = {}
    pass


# register mail here
def register_mail(request):
    pass

