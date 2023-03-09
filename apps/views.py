# all views here are fort the main page functions 

'''
Author == "Jayson"
jaysontechsolutions@gmail.com


#################  All Rights Reserved ###########

'''


from django.shortcuts import render, redirect

# Create your views here.


# login here 
def login_page(request):
    context = {}
    return redirect(request, 'auth_pages/login.html', context)

# 404 here 
def page_not_found(request):
    pass 

def register_mail(request):
    pass

