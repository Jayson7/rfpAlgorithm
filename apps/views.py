# all views here are fort the main page functions 

from django.contrib import messages
from django.shortcuts import render, redirect
from authenticator.models import *
from .models import *
from .questionForm import *
from authenticator.views import basic_user_auth_check, basic_user_auth_check_admin, super_user_check
from django_user_agents.utils import get_user_agent
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
    


# Homepage to welcome user
def Homepage(request):
    context = {}
    return render(request, 'pages/home.html', context)




# question 1

def question1(request):
    
    context = {}
    
    user_agent = get_user_agent(request)
    if request.user.is_authenticated:
        browser_prop = request.user_agent.browser 
        device = request.user_agent.device 
        
        user = request.user 
            # locate user on token 
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile).first()
        # to be added later 
        find_device = StoreDevice.objects.filter(browser=browser_prop, device=device).first()
        # print(find_device,'device')
            
            
            
        if token_of_user.verified == True:
                if token_of_user:
                        # prepare question
                    question1 = Questions.objects.filter(id = 1).first()
                            
                    print(question1) 
                            # get answers ans send form to frontend
                    form = Question1Form(request.POST)
                    if request.method =='POST':
                                if form.is_valid():
                                    forms = form.save(commit=False) 
                                    forms.mom =token_of_user
                                    forms.token =token_of_user
                                    forms.username_used = token_of_user
                                    forms.question = question1
                                    
                                    forms.save()
                                    print(forms.age)
                                    x = int(forms.age)  
                                    if x <= 19:
                                        disease = Disease(
                                            disease = 'anaemia',
                                            user_diagnosed = token_of_user.full_name,
                                            points = 1
                                        )
                                        disease.save()
                                        
                                        
                                        
                                    elif x >= 20 and x <= 35:
                                        pass 
                                    
                                    
                                    elif x > 35 and x < 40:
                                        disease = Disease(
                                            disease = 'thrombosis',
                                            user_diagnosed = token_of_user,
                                            points = 1
                                        )
                                        disease.save()
                                        
                                        disease2 = Disease(
                                            disease = 'intrahepatic cholestasis',
                                            user_diagnosed = token_of_user,
                                            points = 1
                                        )
                                        disease2.save()
                                        
                                    elif x >=40:
                                        disease = Disease(
                                            disease = 'Diabetes Mellitus',
                                            user_diagnosed = token_of_user,
                                            points = 1
                                        )
                                        disease.save()
                                        
                                        disease2 = Disease(
                                            disease = 'preeclampsia',
                                            user_diagnosed = token_of_user,
                                            points = 1
                                        )
                                        
                                        disease2.save()
                                        
                                        disease3 = Disease(
                                            disease = 'thrombosis',
                                            user_diagnosed = token_of_user,
                                            points = 1
                                        )
                                        disease3.save()
                                        
                                        disease4 = Disease(
                                            disease = 'intrahepatic cholestasis',
                                            user_diagnosed = token_of_user,
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
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question1.html', context)






# question 2

def question2(request):
    
    context = {}
    
    user_agent = get_user_agent(request)
    if request.user.is_authenticated:
        browser_prop = request.user_agent.browser 
        device = request.user_agent.device 
        
        user = request.user 
            # locate user on token 
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile).first()
        # to be added later 
        find_device = StoreDevice.objects.filter(browser=browser_prop, device=device).first()
        # print(find_device,'device')
            
        # query question 1 (check if the person did question 1)
        try:
            
            query_q1 = Question1Model.objects.get(token=token_of_user)   
            if query_q1:
                pass 
            else:
                messages.warming(request, 'Not allowed')
                return redirect('login')
        
        except:
            messages.warming(request, 'Not allowed')
            return redirect('login')
        if token_of_user.verified == True:
                if token_of_user and query_q1:
                        # prepare question
                    question2 = Questions.objects.filter(id = 2).first()
                            
                    print(question1) 
                    # get answers ans send form to frontend
                    form = Question2Form(request.POST, request.FILES)
                    if request.method =='POST':
                        
                                if form.is_valid():
                                    forms = form.save(commit=False)
                                    # try coversions 
                                    try:
                                        height  = float(forms.height)
                                        weight = float(forms.weight)
                                        
                                    except:
                                        messages.warning(request, 'No playing around')
                                        return redirect('login')  
                                    # add up missing form fields and calculate BMI
                                    
                                    height  = forms.height
                                    weight = forms.weight 
                                    forms.question = question2
                                    
                                    # calculate BMI
                                    
                                    height_pow = height ** 2
                                    bmi = weight / height_pow
                                    
                                    if bmi < 18.5:
                                        forms.BMI = 'Under Weight'
                                    elif bmi >= 18.5 and bmi <= 24.9:
                                        forms.BMI = 'Mormal'
                                    elif bmi >= 25 and bmi <= 29.9:
                                        forms.BMI = 'Over Weight'
                                    elif bmi >= 30 and bmi <= 34.9:
                                        forms.BMI = 'Obesity (Class I)'                   
                                    elif bmi >= 35 and bmi <= 39.9:
                                        forms.BMI = 'Obesity (Class II)'                                       
                                    elif bmi >= 40:
                                        forms.BMI = 'Obesity (Extreme Obesity)'    
                                    
                                    forms.token = token_of_user
                                    forms.save()
                      
                                        
                                    return redirect('question3')
                                else:
                                    form = Question2Form(request.post)
                                    
                            # send question and answer to view
                    context['question'] = question2
                    context['form'] = form
                else:
                    messages.warning(request, 'Access denied')
                    return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question2.html', context)





# ##############################################################################
# question 3


def question3(request):
    
    context = {}
    
    user_agent = get_user_agent(request)
    
    if request.user.is_authenticated:
        browser_prop = request.user_agent.browser 
        device = request.user_agent.device 
        
        user = request.user 
            # locate user on token 
            
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile).first()
        # to be added later 
        find_device = StoreDevice.objects.filter(browser=browser_prop, device=device).first()
        # print(find_device,'device')
            
        # query question 2 (check if the person did question 1)
        try:

            query_q2 = Question2Model.objects.get(token=token_of_user)
            if query_q2:
                pass 
            else:
                messages.warming(request, 'Not allowed')
                return redirect('login')
        
        except:
            messages.warming(request, 'Not allowed')
            return redirect('login')
        
        if token_of_user.verified == True:
                if token_of_user and query_q2:
                    # prepare question
                    question3 = Questions.objects.filter(id = 3).first()
                    
                    print(question3) 
                    context['question'] = question3
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question3)
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                            Answer.objects.filter(pk=int(i)).update(verified=True, user_print=token_of_user)
                        return redirect('question4')
                        # send question and answer to view
                
               
                else:
                    messages.warning(request, 'Access denied')
                    return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question3.html', context)

