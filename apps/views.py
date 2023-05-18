# all views here are fort the main page functions 

from django.contrib import messages
from django.shortcuts import render, redirect
from authenticator.models import *
from .models import *
from .questionForm import *

from django_user_agents.utils import get_user_agent
from django.db.models import F
# Create your views here.


def details(request, pk):
    context = {}
    
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
    

    if request.user.is_authenticated:
     
        full_name = request.session['details'][2]
        
        user = request.user 
            # locate user on token 
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name=full_name).first()
        # to be added later 

            
            
        if token_of_user.verified == True:
                if token_of_user:
                        # prepare question
                    question1 = Questions.objects.filter(id = 1).first()
                            
             
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
                                    
                                    disease = Disease(
                                            disease = 'thrombosis',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease.save()
                                        
                                    disease2 = Disease(
                                            disease = 'Intrahepatic cholestasis',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease2.save()
                                    
                                    disease3 = Disease(
                                            disease = 'Diabetes Mellitus',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease3.save()
                                        
                                    disease4 = Disease(
                                            disease = 'preeclampsia',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease4.save()
                                    
                                    disease5 = Disease(
                                            disease = 'Thyroid disorders',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease5.save()
                                    
                                    disease6 = Disease(
                                            disease = 'Hyperemesis gravidarum',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease6.save()                                    
                                    disease7 = Disease(
                                            disease = 'Anaemia',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease7.save()      
                                    disease8 = Disease(
                                            disease = 'General mental health assesment',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease8.save()
                                    
                                    disease9 = Disease(
                                            disease = 'Anxiety',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease9.save()
                                    
                                    disease10 = Disease(
                                            disease = 'Depression',
                                            user_diagnosed = token_of_user,
                                            points = 0
                                        )
                                    disease10.save()
                                    
                                    
                                    
                                    print(forms.age)
                                    x = int(forms.age)  
                                    if x <= 19:
                                       
                                       d =  Disease.objects.get(disease="Anaemia", user_diagnosed=token_of_user)
                                       d.points += 1
                                       d.save()
                                        
                                        
                                    elif x >= 20 and x <= 35:
                                        pass 
                                    
                                    
                                    elif x > 35 and x < 40:
                                        d = Disease.objects.get(disease = 'thrombosis', user_diagnosed=token_of_user)
                                        d.points += 1
                                        d.save()
                                        d = Disease.objects.get(disease = 'Intrahepatic cholestasis', user_diagnosed=token_of_user)
                                        d.points += 1
                                        d.save()
                                    elif x >=40:
                             
                                        d = Disease.objects.get(disease = 'thrombosis', user_diagnosed=token_of_user)
                                        d.points += 2
                                        d.save()
                                    # create questions sessions and modify
                                    
                                    request.session['questions_answered'] = [1]
                                    request.session.modified = True
                                      
                                        
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
    
    
    if request.user.is_authenticated:

        
        user = request.user 
        full_name = request.session['details'][2]
        print(full_name)
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name=full_name).first()
 
    
        # verify if user answered question 1
 
        if token_of_user.verified == True:
                if token_of_user:
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

                                    request.session['questions_answered'] = [1,2]
                                    request.session.modified = True
                                        
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
    
    
    
    if request.user.is_authenticated:

        user = request.user 
            # locate user on token 
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()
        print(token_of_user)
        # to be added later 

            
        
        if token_of_user.verified == True:
                if token_of_user:
                    # prepare question
                    question3 = Questions.objects.filter(id = 3).first()
                    
  
                    context['question'] = question3
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question3)
                   
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           for ans in check_answers:
                                if ans.answer == 'Asian':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points += 1
                                    d.save()
                                    
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                    d.points += 1
                                    d.save()
                                   
                                   
                                elif ans.answer == 'Black race':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                    d.points += 1
                                    d.save()
                                elif ans.answer == 'Latino':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points += 1
                                    d.save()
                                    
                                    d= Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                    d.points += 1
                                    d.save()
                                    
                                elif ans.answer == 'Middle Eastern / Arab':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                    d.points += 1
                                    d.save()
                                elif ans.answer == 'Other':
                                    pass
                                elif ans.answer == 'Native American':
                                    d = Disease.objects.get(disease = 'Diabetes Mellitus').update(points=F("points") + 1)
                                    d.points +=1
                                    d.save()
                                    return redirect('question3')
                                elif ans.answer == 'White race':
                                    pass 
                                
                                    
                                    
                                   
                                request.session['questions_answered'] = [1,2,3]
                                request.session.modified = True
                                
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




# ##############################################################################
# question 4


def question4(request):
    
    context = {}
    

    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()
        
      
        
        if token_of_user.verified == True:
        # if request.user:
                if token_of_user:
                    # prepare question
                    question4 = Questions.objects.filter(id = 4).first()
                    
                    context['question'] = question4
                    context['question_tag'] = 'Question 4'
                    context['question_tag_eng'] = 'Four'
                    
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question4)
                    
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'First pregnancy or gestational loss less than 20 weeks':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Hyperemesis gravidarum')
                                    d.points +=1
                                    d.save()

                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 1
                                    d.save()

                                elif ans.answer == '2 deliveries':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points+= 1
                                    d.save()
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anaemia')
                                    d.points += 1
                                    d.save()
                               
                                elif ans.answer == '3 or more deliveries':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()

                                
                                
                                request.session['questions_answered'] = [1,2,3,4]
                                request.session.modified = True
                                # print(request.session['questions_answered'])
                                    
                                   

                        return redirect('question5')
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
    return render(request, 'questions/question4.html', context)





# ##############################################################################
# question 5


def question5(request):

    context = {}
    
   
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()
        
      
        
        if token_of_user.verified == True:
        # if request.user:
                if token_of_user:
                    # prepare question
                    question5 = Questions.objects.filter(id = 5).first()
                    
                    context['question'] = question5
                    context['question_tag'] = 'Question 5'
                    context['question_tag_eng'] = 'Five'
                    
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question5)
                    
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'No':
                                    pass
                                elif ans.answer == 'Yes':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points+= 1
                                    d.save()
                           
                                elif ans.answer == 'I am not currently pregnant':
                                    pass
                                
                                    
                                request.session['questions_answered'] = [1,2,3,4,5]
                                request.session.modified = True
                      
    

                        return redirect('question6')
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
    return render(request, 'questions/question4.html', context)



# ##############################################################################
# question 6


def question6(request):
    
    context = {}

    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()
        

        if token_of_user.verified == True:
        # if request.user:
                # if token_of_user:
                    # prepare question
                    question6 = Questions.objects.filter(id = 6).first()
                    
                    context['question'] = question6
                    context['question_tag'] = 'Question 6'
                    context['question_tag_eng'] = 'Six'
                    
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question6)
                    
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'Yes':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Hyperemesis gravidarum')
                                    d.points +=1
                                    d.save()

                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 1
                                    d.save()
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anaemia')
                                    d.points += 1
                                    d.save()
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()
                                elif ans.answer == 'No' or ans.answer == 'I am not currently pregnant':
                                    pass 
                                
                                
                                request.session['questions_answered'] = [1,2,3,4,5,6]
                                request.session.modified = True
                      

                        return redirect('question7')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Access denied')
                #     return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question4.html', context)




# ###############################################################################################
# question 7


def question7(request):
    
    context = {}

    if request.user.is_authenticated:

        user = request.user 
        # locate user on token 

        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()
        
        
        if request.user:
                # if token_of_user:
                    # prepare question
                    question7 = Questions.objects.filter(id = 7).first()
                    
                    context['question'] = question7
                    context['question_tag'] = 'Question 7'
                    context['question_tag_eng'] = 'Seven'
                    
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question7)
                    
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'Yes, I have been diagnosed with deep vein thrombosis AND I am currently on anticoagulant treatment.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 100 
                                    d.save()
                                
                                
                                elif ans.answer == 'No, I am not on anticoagulant treatment for a previous deep vein thrombosis.':
                                    pass
           
                                request.session['questions_answered'] = [1,2,3,4,5,6,7]
                                request.session.modified = True

                        return redirect('question8')
                        # send question and answer to view

                # else:
                #     messages.warning(request, 'Access denied')
                #     return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question4.html', context)




# ##############################################################################

# question 8


def question8(request):
    
    context = {}
    
    
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()

        if request.user:
                # if token_of_user:
                    # prepare question
                    question8 = Questions.objects.filter(id = 8).first()
                    
                    context['question'] = question8
                    context['question_tag'] = 'Question 8'
                    context['question_tag_eng'] = 'Eight'
                    
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question8)
                    
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'Yes, I have been diagnosed with antithrombin deficiency or antiphospholipid syndrome.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 100 
                                    d.save()


                                elif ans.answer == 'No, I have not been diagnosed with antithrombin deficiency or antiphospholipid syndrome.':
                                    pass
                            
                                    
                                    
                        request.session['questions_answered'] = [1,2,3,4,5,6,7,8]
                        request.session.modified = True

                        return redirect('question9')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Access denied')
                #     return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question4.html', context)



# ##############################################################################
# question 9


def question9(request):
    
    context = {}
 
    if request.user.is_authenticated:


        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()

        if request.user:
                # if token_of_user:
                    # prepare question
                    question9 = Questions.objects.filter(id = 9).first()
                    
                    context['question'] = question9
                    context['question_tag'] = 'Question 9'
                    context['question_tag_eng'] = 'Nine'
                    
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question9)
                    
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'Yes, I was diagnosed with deep vein thrombosis AND I am NOT currently on anticoagulant treatment (The cause of the thrombosis was a recent surgery).':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()


                                elif ans.answer == 'Yes, I was diagnosed with deep vein thrombosis AND I am NOT currently on anticoagulant treatment (The cause of the thrombosis is unknown or different from surgery).':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 4
                                    d.save()

                               
                                elif ans.answer == 'No, I have never had deep vein thrombosis.':
                                    pass 
             
                                
                                request.session['questions_answered'] = [1,2,3,4,5,6,7,8,9]
                                request.session.modified = True
                      
    

                        return redirect('question10')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Access denied')
                #     return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question4.html', context)



# ##############################################################################
# question 10


def question10(request):
    
    context = {}
  
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()

        if request.user:
                # if token_of_user:
                    # prepare question
                    question10 = Questions.objects.filter(id = 10).first()
                    
                    context['question'] = question10
                    context['question_tag'] = 'Question 10'
                    context['question_tag_eng'] = 'Ten'
                    
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question10)
                    
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'Homozygous factor V Leiden':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()


                                elif ans.answer == 'Heterozygous factor V Leiden':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()
                               
                                elif ans.answer == ' Homozygous prothrombin gene mutation':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()                                
                                elif ans.answer == 'Heterozygous prothrombin gene mutation':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()                                
                                elif ans.answer == ' Protein C deficiency':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()
                                elif ans.answer == ' Protein S deficiency':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()
                                elif ans.answer == 'Obstetric antiphospholipid syndrome':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()
                                elif ans.answer == 'Combination of Heterozygous factor V Leiden and  Heterozygous prothrombin gene mutation':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()
                                    
                                request.session['questions_answered'] = [1,2,3,4,5,6,7,8,9, 10]
                                request.session.modified = True
                        return redirect('questionCs')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Access denied')
                #     return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question5.html', context)



# ##############################################################################
# question 11, 12, 13, 14


def questionCombined(request):
    
    context = {}
    
    
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()
        
      
        
        if token_of_user.verified == True:
        # if request.user:
                # if token_of_user:
                    # prepare question
                    question11 = Questions.objects.filter(id = 11).first()
                    question12 = Questions.objects.filter(id = 12).first()
                    question13 = Questions.objects.filter(id = 13).first()
                    question14 = Questions.objects.filter(id = 14).first()
                    
                    context['question1'] = question11
                    context['question2'] = question12
                    context['question3'] = question13
                    context['question4'] = question14
                    context['question_tag'] = 'Question 11, 12, 13 & 14'
                    context['question_tag_eng'] = 'Eleven, Twelve, Thirteen and Fourteen'
                    
                    # get answers ans send form to frontend
                    
                    x_list1 = Answer.objects.filter(question=question11)
                    x_list2 = Answer.objects.filter(question=question12)
                    x_list3 = Answer.objects.filter(question=question13)
                    x_list4 = Answer.objects.filter(question=question14)
                    
                 
                    context['xlist1'] = x_list1
                    context['xlist2'] = x_list2
                    context['xlist3'] = x_list3
                    context['xlist4'] = x_list4
                    if request.method =='POST':
                        
                        list_checked1 = request.POST.getlist('xlist_boxes')
                        list_checked2 = request.POST.getlist('xlist_boxes')
                        list_checked3 = request.POST.getlist('xlist_boxes')
                        list_checked4 = request.POST.getlist('xlist_boxes')
                        
                        
                        for i in list_checked1:
                           
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           for ans in check_answers:

                                if ans.answer == 'Active systemic lupus erythematosus':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()

                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 2
                                    d.save()

                                elif ans.answer == 'Active heart failure':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                               
                                elif ans.answer == 'Previous thyroid pathology with current treatment':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                    d.points += 100
                                    d.save()
                                    
                                    
                                elif ans.answer == 'Sickle cell anemia or thalassemia':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                                    
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anaemia')
                                    d.points +=100
                                    d.save()
                                    # 
                                elif ans.answer == 'Other hemoglobinopathy':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anaemia')
                                    d.points +=100
                                    d.save()
                                    
                                elif ans.answer == 'Chronic hypertension (pre-pregnancy)':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 3
                                    d.save()
                                elif ans.answer == 'Polycystic ovary syndrome':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                    d.points += 1
                                    d.save()
                                elif ans.answer == 'Previous treatment with radioactive iodine':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                    d.points += 1
                                    d.save()
                                    
                                elif ans.answer == 'Chronic kidney disease':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 2
                                    d.save()
                                elif ans.answer == 'Active inflammatory bowel disease':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                                    
                                elif ans.answer == 'Chronic hepatitis C':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Previous thyroidectomy':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                    d.points += 1
                                    d.save()
                                    
                                elif ans.answer == 'Active inflammatory polyarthritis':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                                    
                                elif ans.answer == 'Non-alcoholic fatty liver':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points +=1
                                    d.save()
                                 #  
                                elif ans.answer == 'Goiter':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Type I diabetes mellitus':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points +=2
                                    d.save()
                                    
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disorder')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Previous thyroiditis':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disorder ')
                                    d.points +=1
                                    d.save()
                                elif ans.answer == 'Type 1 diabetes with renal involvement':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points +=1
                                    d.save()
                                elif ans.answer == 'Type II diabetes':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points +=2
                                    d.save()

                                elif ans.answer == 'Active nephrotic syndrome (renal pathology)':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = ' thrombosis')
                                    d.points +=3
                                    d.save()

                                elif ans.answer == 'Obstetric/thrombotic antiphospholipid syndrome':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points +=2
                                    d.save()

                                elif ans.answer == 'Subclinical hypothyroidism':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disorder ')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Active cancer (others)':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                                
                                elif ans.answer == 'Previous inflammatory pathology/surgery affecting iron absorption (celiac disease, current H. pylori infection, or inflammatory bowel disease)':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                    d.points +=1
                                    d.save()

                                
                                
                                    
                        for i in list_checked2:
                            
                            if ans.answer == 'Immobilization (wheelchair, paraplegia)':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Persistent positivity of antiphospholipid antibodies':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                d.points +=1
                                d.save()
                                
                            elif ans.answer == 'Insulin resistance or prediabetes':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Interval between pregnancies < 1 year':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()

                                                        
                            if ans.answer == 'Interval between pregnancies > 10 years)':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Positivity of antithyroid antibodies':
                                pass
                             
                            elif ans.answer == 'Current intravenous drug use':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=3
                                d.save()

                            elif ans.answer == 'Palpable thick venous varices':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()                            
                            elif ans.answer == 'Current smoker':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()     
                                
                            elif ans.answer == 'Preeclampsia in current pregnancy':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()   
                                                         
                            elif ans.answer == 'Palpable thick venous varices':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()                            
                            elif ans.answer == 'Hyperemesis gravidarum in current pregnancy':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disorder')
                                d.points +=1
                                d.save()                            
                            elif ans.answer == 'Currently on treatment with corticosteroids or antipsychotics':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes ')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Previous pregnancy with a baby weighing >4.5 kg':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes ')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'History of liver enzyme abnormalities with oral contraceptives':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'intrahepatic cholestasis')
                                d.points +=1
                                d.save()
                            
                            elif ans.answer == 'Previous intravenous iron therapy':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()
                            elif ans.answer == 'Following a vegetarian or vegan diet':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()
                                
                            elif ans.answer == 'Recent history of significant bleeding':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()

     
                                    
                        for i in list_checked4:
                           
                            if ans.answer == 'thyroid disorder Familial autoimmune':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disease')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Preeclampsia':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()
                                
                            elif ans.answer == 'Mother/sisters or daughters with intrahepatic cholestasis':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = ' intrahepatic cholestasis')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Deep vein thrombosis':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()

                                                        
                            if ans.answer == 'Mother/sisters or daughters with hyperemesis gravidarum':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Hyperemesis gravidarum')
                                d.points +=1
                                d.save()

                            if ans.answer == 'Mother/sisters or daughters with diabetes mellitus':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes')
                                d.points +=1
                                d.save()

                            
                                                         
                        for i in list_checked3:
                            if ans.answer == 'Preeclampsia or chronic arterial hypertension':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                d.points +=2
                                d.save()

                            elif ans.answer == 'Persistent positivity of antiphospholipid antibodies':
                                pass
                                
                            elif ans.answer == 'Gestational diabetes':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Hyperemesis gravidarum':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()

                                                        
                            if ans.answer == 'Hypothyroidism/hyperthyroidism':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = ' thyroid disorder')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Anaemia':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'anaemia')
                                d.points +=1
                                d.save()
                             
                            elif ans.answer == 'Intrahepatic cholestasis':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'None of the above':
                                pass
                                                         
                            elif ans.answer == 'I have not been pregnant':
                                pass                  
                            
                            elif ans.answer == 'Familial genetic thrombophilia (including factor V Leiden, mutation of the prothrombin gene, protein C or S)':
                                pass
                            
                     
                                
   

                                request.session['questions_answered'] = [1,2,3,4,5,6,7,8,9, 10, 11, 13, 14]
                                request.session.modified = True
                                
                                                                       

                        return redirect('question16')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Access denied')
                #     return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question6.html', context)


# ##############################################################################
# question 15


def question15(request):
    
    context = {}
    
    
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()

        if request.user:
                # if token_of_user:
                    # prepare question
                    question15 = Questions.objects.filter(id = 15).first()
                    
                    context['question'] = question15
                    context['question_tag'] = 'Question 15'
                    context['question_tag_eng'] = 'Fifteen'
                    
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question15)
                    
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'Yes':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Hyperemesis gravidarum')
                                    d.points +=1
                                    d.save()

                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 1
                                    d.save()

                                elif ans.answer == 'No':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points+= 1
                                    d.save()
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anaemia')
                                    d.points += 1
                                    d.save()
                               
                                elif ans.answer == 'I am not currently pregnant':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()

                                
                                
                                    
                                    
                                request.session['questions_answered'] = [1,2,3,4,5,6,7,8,9, 10, 11, 13,14,15,16]
                                request.session.modified = True
                                
                                    
                                   

                        return redirect('generate_results')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Access denied')
                #     return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question5.html', context)




# ##############################################################################
# question 16


def question16(request):
    
    context = {}
    
    
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        reg_instance_profile = RegisterClient.objects.filter(username=user).first()
        token_of_user = UserLoginToken.objects.filter(username=reg_instance_profile, full_name = full_name).first()

        if request.user:
                # if token_of_user:
                    # prepare question
                    question16 = Questions.objects.filter(id = 16).first()
                    
                    context['question'] = question16
                    context['question_tag'] = 'Question 16'
                    context['question_tag_eng'] = 'Sixteen'
                    
                    # get answers ans send form to frontend
                    
                    x_list = Answer.objects.filter(question=question16)
                    
                    print(x_list) 
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        print(list_checked)
                        
                        for i in list_checked:
                           check_answers = Answer.objects.filter(pk=int(i))
                           check_answers.update(verified=True, user_print=token_of_user)
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'Yes':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Hyperemesis gravidarum')
                                    d.points +=1
                                    d.save()

                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 1
                                    d.save()

                                elif ans.answer == 'No':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points+= 1
                                    d.save()
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anaemia')
                                    d.points += 1
                                    d.save()
                               
                                elif ans.answer == 'I am not currently pregnant':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()

                                
                                
                                    
                                    
                                   

                        return redirect('generate_results')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Access denied')
                #     return redirect('login')           
        else:
                messages.warning(request, 'User not verified')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question7.html', context)





def permanemtStorage(request):
    # session info
    
    
    user = request.user
    if user.is_authenticated():
        pass
        
        
        
        
    else:
        return redirect('login')
    
    # activate storage of results and check for validity 
    # 1. token check 
    token_check = UserLoginToken.objects.filter(username=user, verified=True).filter()
def generateresult_user(request):
    pass 

def activate_deletions(request):
    pass