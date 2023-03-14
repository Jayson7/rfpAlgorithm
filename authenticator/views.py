from django.shortcuts import render, redirect

# Create your views here.



# login here 
def login_page(request):
    context = {}
    
    return render(request, 'auth_pages/user_login.html', context)



# register mail here
def register_mail(request):
    pass

