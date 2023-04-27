# all views here are fort the main page functions 

from django.contrib import messages
from django.shortcuts import render, redirect
from authenticator.models import *
from .models import *
from .questionForm import *
from authenticator.views import basic_user_auth_check, basic_user_auth_check_admin, super_user_check
# Create your views here.



def details(request, pk):
    context = {}
    basic_user_auth_check_admin(request)
    super_user_check(request)
    
    user = RegisterClient.objects.get(id=pk)
    
    if user:
        try:
            # password profile
            password_profile = PasswordStorage.objects.get(client=user)
            print(password_profile) 
            
            print(user)
            if password_profile and user:
                context['password_profile'] = password_profile
                context['user_profile'] = user
            
        except:
            messages.warning(request, 'User has no generated access')
                        # password profile
            # password_profile = PasswordStorage.objects.get(client=user)
            # print(password_profile) 
            
            print(user)
            if user:
                context['password_profile'] = 'none'
                context['user_profile'] = user        
        else:
            pass 
        
    return render(request, 'admin_pages/details.html', context)

        


def choose_test(request):
    pass 


# 404 here 
def page_not_found(request):
    pass 


def question_controller(request):
  
    pass 

    
    
# admin privileges needed for managing users 
def manage_user(request):
    user = request.user 
    context = {}
    if user.is_authenticated:
        if user.is_superuser:
            all_user = RegisterClient.objects.all()
            pass_profile = PasswordStorage.objects.all()
            context['user'] = all_user
            context['pass_profile'] = pass_profile
            
        else:
            messages.warning(request, 'That will not work')
            return redirect('login')
    else:
        messages.warning(request, 'Access denied')
        return redirect('admin_login')        

    return render (request, 'admin_pages/manage_user.html', context)
    





# question 1

def question1(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user 
            # locate user on token 
        try:
            token_of_user = UserLoginToken.objects.filter(username=user).first()
            if token_of_user:
                    # prepare question
                question1 = Questions.objects.filter(id = 1).first()
                        
                print(question1) 
                        # get answers ans send form to frontend
                form = Question1Form()
                if request.method =='POST':
                            if form.is_valid():
                                forms = form.save(commit=False) 
                                forms.mom =token_of_user.full_name
                                forms.token =token_of_user.token 
                                form.username_used = token_of_user.username
                                form.question = question1.question
                                
                                form.save()
                                print(forms.age)
                                x = int(forms.age)  
                                if x <= 19:
                                    disease = Disease.create(
                                        disease = 'anaemia',
                                        user_diagnosed = 'token.full_name',
                                        points = 1
                                    )
                                    disease.save()
                                    
                                    
                                    
                                elif x >= 20 and x <= 35:
                                    pass 
                                
                                elif x > 35 and x < 40:
                                    disease = Disease.create(
                                        disease = 'thrombosis',
                                        user_diagnosed = 'token.full_name',
                                        points = 1
                                    )
                                    disease.save()
                                    
                                    disease2 = Disease.create(
                                        disease = 'intrahepatic cholestasis',
                                        user_diagnosed = 'token.full_name',
                                        points = 1
                                    )
                                    disease2.save()
                                    
                                elif x >=40:
                                    disease = Disease.create(
                                        disease = 'Diabetes Mellitus',
                                        user_diagnosed = 'token.full_name',
                                        points = 1
                                    )
                                    disease.save()
                                    
                                    disease2 = Disease.create(
                                        disease = 'preeclampsia',
                                        user_diagnosed = 'token.full_name',
                                        points = 1
                                    )
                                    
                                    disease2.save()
                                    
                                    disease3 = Disease.create(
                                        disease = 'thrombosis',
                                        user_diagnosed = 'token.full_name',
                                        points = 1
                                    )
                                    disease3.save()
                                    
                                    disease4 = Disease.create(
                                        disease = 'intrahepatic cholestasis',
                                        user_diagnosed = 'token.full_name',
                                        points = 1
                                    )
                                    disease4.save()
                                    
                                    
                                return redirect('question2')
                            else:
                                form = Question1Form(request.post)
                                
                        # send question and answer to view
                context['question'] = question1
                context['form'] = form
            else:
                messages.warning(request, 'Access denied')
                return redirect('login')           
        except:
            return redirect('login')     
    else:
        return redirect('login')
    return render(request, 'questions/question1.html', context)



# question 2
def question2(request):
    context = {}
    # if request.user.is_authenticated:
    user = request.user 
        # loctate user on token 
    try:
            # token_of_user = UserLoginToken.objects.filter(username=user).first()
            
                # prepare question
        question1 = Questions.object.filter(pk = 1)
        print = question1.question 
        question_view = question1.question 

        # prepare answers 
        answers = Answer.objects.filter(question=question_view)
        print(answers)
        context['answers'] = answers 
        # send question and answer to view
        context['question'] = question1
                
    except:
            return redirect('login')     
    # else:
    #     return redirect('login')
    return render(request, 'questions/question1.html', context)


     