from django.shortcuts import render, redirect

# Create your views here.


# login here 
def login_page(request):
    context = {}
    
    return redirect(request, 'auth_pages/login.html', context)



# register mail here
def register_mail(request):
    pass

