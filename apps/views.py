# all views here are fort the main page functions 

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
import datetime 
from authenticator.models import *
from .models import *
from django.http import HttpResponse

#  import auth managers 
from authenticator.views import basic_user_auth_check, basic_user_auth_check_admin, details_checker_questions, deactivate_auth


# remove csrf
from django.views.decorators.csrf import csrf_exempt


# generate pdf 
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


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



# 404 here 
def page_not_found(request):
    pass 


    
# admin privileges needed for managing users 
def manage_user(request):
    user = request.user 
    context = {}
    if user.is_authenticated:
        # segmented data
            
        context['total_patient'] = Result_owner.objects.count()
        context['test_taken'] = Result_owner.objects.count()
        context['hospital'] = RegisterClient.objects.count()
        context['access'] = PasswordStorage.objects.count()
            
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
    
    #   set session expiry 
    
    
    context = {}
    return render(request, 'pages/home.html', context)



# Homepage to welcome user in spanish
def HomepageSpanish(request):
    
    #   set session expiry 
    
    
    context = {}
    return render(request, 'pages/homeSpanish.html', context)



# question 1
@csrf_exempt
def question1(request):
    basic_user_auth_check(request)
    details_checker_questions(request)
    context = {}
    # try:
        
    if request.user.is_authenticated:
       
                # locate user on token 
                token_of_user = request.session['token_ses']
            
                if token_of_user:
                            # prepare question
                        question1 = Questions.objects.filter(id = 1).first()
                                
                                # get answers ans send form to frontend
                    
                        if request.method =='POST':
                                    age = request.POST['age']
                                    # convert to integer
                                    try:
                                        x =  int(age)
                                    except:
                                        messages.warning(request, 'Invalid input')
                                        return redirect('question1')
                            
                                    request.session['age'] = x                
                                        
                                        
                                        
                                        
                                        # delete all previous diseases 
                                        
                                    try:
                                            disease = Disease.objects.filter(user_diagnosed=request.session['token_ses'])
                                            
                                            for i in disease:
                                                i.delete()
                                    except:
                                            pass         
                                        
                                        
                                        
                                        
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
                                        
                                    disease11 = Disease(
                                                disease = 'pregnancy wellbeing',
                                                user_diagnosed = token_of_user,
                                                points = 0,
                                            )
                                    disease11.save()
                                        
                                    
                                    # create data into session
                                    
                                
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
                                        
                                        
                                    request.session['q1'] = [x]
                                        
                                        
                                    request.session['questions_answered'] = [1]
                                    request.session.modified = True
                                        
                                            
                                    return redirect('question2')
                        
                                        
                                # send question and answer to view
                        context['question'] = question1
                
                else:
                        messages.warning(request, 'Access denied')
                        
                        request.session.flush()
                        logout(request)
                        return redirect('login')           

         
    
    # except:
    #     messages.warning(request, 'User unverified')
    #     return redirect('login')
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question1.html', context)






# question 2

def question2(request):
    basic_user_auth_check(request)
    details_checker_questions(request)
    context = {}
    
    
    if request.user.is_authenticated:

        # try: 
            user = request.user 
            token_of_user = request.session['token_ses']
            # verify if user answered question 1
    
            if token_of_user:
    
                            # prepare question
                        question2 = Questions.objects.filter(id = 2).first()

                
                        # get answers ans send form to frontend
            
                        if request.method =='POST':
                            
                                        height = request.POST['height']
                                        weight = request.POST['weight']

    
                                        # try coversions 
                                     
                                        height  = float(height)
                                        weight = float(weight)
                                            
                                   
                                        # add up missing form fields and calculate BMI
                                        
                                    
                                        
                                        
                                        # calculate BMI
                                        
                                        height_pow = height ** 2
                                        bmi = weight / height_pow
                                        
                                        if bmi < 18.5:
                                            BMI_rate = 'Under Weight'
                                        elif bmi >= 18.5 and bmi <= 24.9:
                                            BMI_rate = 'Mormal'
                                        elif bmi >= 25 and bmi <= 29.9:
                                            BMI_rate = 'Over Weight'
                                        elif bmi >= 30 and bmi <= 34.9:
                                            BMI_rate = 'Obesity (Class I)'                   
                                        elif bmi >= 35 and bmi <= 39.9:
                                            BMI_rate = 'Obesity (Class II)'                                       
                                        elif bmi >= 40:
                                            BMI_rate = 'Obesity (Extreme Obesity)'    
                                        
                    
                                        request.session['q2'] = [BMI_rate, height, weight]
                                        
                                        # check current user for bmi 
                                        
                                        try:
                                            bmi_check = BMI.objects.filter(token=token_of_user, full_name=request.session['details'][2])
                                            bmi_check.delete()
                                        
                                        except:
                                            pass 
                                        
                                                 
                                        if bmi >= 30:
                                            d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                            d.points += 1
                                            d.save()
                                            
                                            d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Hyperemesis gravidarum')
                                            d.points +=1
                                            d.save()          

                                            d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                            d.points += 1
                                            d.save()
                                        
                                        elif bmi >= 35:
                                            d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                            d.points += 1
                                            d.save()
                                        
                                        elif bmi >= 40:
                                            d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                            d.points += 2
                                            d.save()
                                        
                                        # save bmi to database
                                        
                                     
            
                                        bmi = BMI(
                                                bmi = BMI_rate,
                                                height =  height,
                                                weight =  weight,
                                                token = request.session['token_ses'],
                                                full_name =  request.session['details'][2],  
                                            )
                                        bmi.save()
                                      
                                            
                                         
                                        
                                        
                                        request.session['questions_answered'] = [1,2]
                                        request.session.modified = True
                                            
                                        return redirect('question3')
                    
                                        
                                # send question and answer to view
                        context['question'] = question2
                    
                        
            else:
                    messages.warning(request, 'User not verified')
            # except:
            #     messages.warning(request, 'Error')
            #     
            # request.session.flush()
            # logout(request)
            # return redirect('login')     
            
        # except:
        #     messages.warning(request, 'User verification error') 
        #     return redirect('login')
        
    else:
            messages.warning(request, 'Authentication required')
            return redirect('login')
    return render(request, 'questions/question2.html', context)





# ##############################################################################
# question 3


def question3(request):
    
    basic_user_auth_check(request)
    details_checker_questions(request)
    context = {}
   
    if request.user.is_authenticated:
        user = request.user 
        token_of_user = request.session['token_ses']
  
        
        if token_of_user:

                        question3 = Questions.objects.filter(id = 3).first()
                        
    
                        context['question'] = question3
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question3)
                        sorted_queries = sorted(x_list, key=lambda q: str(q.answer))
                        x_list = sorted_queries
                        context['xlist'] = x_list
                        
                        if 'question3' in request.session:
                            del request.session['question3']
                        else:
                                pass 
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                            
                            
                            question3Session = request.session['question3'] = []
                            
                            for i in list_checked:
                                check_answers = Answer.objects.filter(pk=int(i))
                                question3Session.append(str(check_answers.first())) 
                        
                            
                            
                            
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
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                        d.points += 1
                                        d.save()
                                    
                                    elif ans.answer == 'White race':
                                        pass 
                                    
                                        
                                        
                                    
                                    request.session['questions_answered'] = [1,2,3]
                                    request.session.modified = True
                                    
                            return redirect('question4')
                            # send question and answer to view
                    
                
                    # else:
                        # messages.warning(request, 'Access denied')
                        # 
                        # request.session.flush()
                        # logout(request)
                        # return redirect('login')           
        else:
                    messages.warning(request, 'User not verified')
            # except:
            #     messages.warning(request, 'Error')
            #     
            # request.session.flush()
            # logout(request)
            # return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question3.html', context)




# ##############################################################################
# question 4


def question4(request):
        
    basic_user_auth_check(request)
    details_checker_questions(request)
    
    context = {}
 

    if request.user.is_authenticated:

            user = request.user 
            token_of_user = request.session['token_ses']
        
            if token_of_user:
        
                        # prepare question
                        question4 = Questions.objects.filter(id = 4).first()
                        
                        context['question'] = question4
                        context['question_tag'] = 'Question 4'
                        context['question_tag_eng'] = 'Four'
                        
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question4)
                        
                        if 'question4' in request.session:
                            del request.session['question4']
                        else:
                            pass
            
                        context['xlist'] = x_list
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                        
                            question4Session = request.session['question4'] = []
                            
                            for i in list_checked:
                                check_answers = Answer.objects.filter(pk=int(i))
                                question4Session.append(str(check_answers.first())) 
                            
                            
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

                                    else:
                                        pass
                                    
                                    request.session['questions_answered'] = [1,2,3,4]
                                    request.session.modified = True
                                    # print(request.session['questions_answered'])
                                        
                                    

                            return redirect('question5')
                            # send question and answer to view
                    
                        
            else:
                    messages.warning(request, 'User not verified')

    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question5.html', context)





# ##############################################################################
# question 5


def question5(request):

    context = {}
    
    basic_user_auth_check(request)
    details_checker_questions(request)

        
    if request.user.is_authenticated:

            token_of_user = request.session['token_ses']
            user = request.user 
            # locate user on token 
                
            full_name = request.session['details'][2]
            # try:
            
            if 'question5' in request.session:
                del request.session['question5']
            else:
                    pass
            
    
            if token_of_user:
        
                        # prepare question
                        question5 = Questions.objects.filter(id = 5).first()
                        
                        context['question'] = question5
                        context['question_tag'] = 'Question 5'
                        context['question_tag_eng'] = 'Five'
                        
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question5)
                        
                    
                        context['xlist'] = x_list
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                            question5Session = request.session['question5'] = []
                            
                            for i in list_checked:
                                check_answers = Answer.objects.filter(pk=int(i))
                                question5Session.append(str(check_answers.first())) 
                            
                            
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
                    messages.warning(request, 'User not verified')
            # except:
            #     messages.warning(request, 'Error')
            #     
            # request.session.flush()
            # logout(request)
            # return redirect('login')     
    else:
            messages.warning(request, 'Authentication required')
            return redirect('login')

    
    return render(request, 'questions/question4.html', context)



# ##############################################################################
# question 6


def question6(request):
    
    context = {}

    basic_user_auth_check(request)
    details_checker_questions(request)
    
    

    if request.user.is_authenticated:

            
            user = request.user 
                # locate user on token 
                
            full_name = request.session['details'][2]
            # try:
            token_of_user = request.session['token_ses']
            
            if 'question6' in request.session:
                del request.session['question6']
            else:
                pass
            
        
            

            if token_of_user:
            # if request.user:
                    # if token_of_user:
                        # prepare question
                        question6 = Questions.objects.filter(id = 6).first()
                        
                        context['question'] = question6
                        context['question_tag'] = 'Question 6'
                        context['question_tag_eng'] = 'Six'
                        
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question6)
                        
                    
                        context['xlist'] = x_list
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                            question6Session = request.session['question6'] = []
                            
                            for i in list_checked:
                                check_answers = Answer.objects.filter(pk=int(i))
                                question6Session.append(str(check_answers.first())) 
                            
                            
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
                    #     
                    # request.session.flush()
                    # logout(request)
                    # return redirect('login')           
            else:
                    messages.warning(request, 'User not verified')
            # except:
            #     messages.warning(request, 'Error')
            #     
            # request.session.flush()
            # logout(request)
            # return redirect('login')     
    else:
            messages.warning(request, 'Authentication required')
            return redirect('login')
        

    
    return render(request, 'questions/question4.html', context)




# ###############################################################################################
# question 7


def question7(request):
    basic_user_auth_check(request)
    details_checker_questions(request)
    
    context = {}

            
    if request.user.is_authenticated:

            user = request.user 
            # locate user on token 

            full_name = request.session['details'][2]
            # try:
            if 'question7' in request.session:
                del request.session['question7']
            else:
                pass
            
                token_of_user = request.session['token_ses']
            
            
            if request.user:
                    # if token_of_user:
                        # prepare question
                        question7 = Questions.objects.filter(id = 7).first()
                        
                        context['question'] = question7
                        context['question_tag'] = 'Question 7'
                        context['question_tag_eng'] = 'Seven'
                        
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question7)
                        
                    
                        context['xlist'] = x_list
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                            question7Session = request.session['question7'] = []
                            
                            for i in list_checked:
                                check_answers = Answer.objects.filter(pk=int(i))
            
                                question7Session.append(str(check_answers.first())) 
                            
                            
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
                    #     
                    # request.session.flush()
                    # logout(request)
                    # return redirect('login')           
            else:
                    messages.warning(request, 'User not verified')
            # except:
            #     messages.warning(request, 'Error')
            #     
            # request.session.flush()
            # logout(request)
            # return redirect('login')     
    else:
            messages.warning(request, 'Authentication required')
            return redirect('login')

    return render(request, 'questions/question4.html', context)




# ##############################################################################

# question 8


def question8(request):
    basic_user_auth_check(request)
    details_checker_questions(request)
    
    context = {}
    
    
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        try:
        
            token_of_user = request.session['token_ses']
            if 'question8' in request.session:
                del request.session['question8']
            else:
                pass
            
                
            print(request.session['question7'])
            
            if request.user:
                    # if token_of_user:
                        # prepare question
                        question8 = Questions.objects.filter(id = 8).first()
                        
                        context['question'] = question8
                        context['question_tag'] = 'Question 8'
                        context['question_tag_eng'] = 'Eight'
                        
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question8)
                        
                    
                        context['xlist'] = x_list
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                            question8Session = request.session['question8'] = []
                            
                            for i in list_checked:
                                check_answers = Answer.objects.filter(pk=int(i))
                                question8Session.append(str(check_answers.first())) 
                            
                            
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
                    #     
                    # request.session.flush()
                    # logout(request)
                    # return redirect('login')           
            else:
                    messages.warning(request, 'User not verified')
        except:
            messages.warning(request, 'Error')
            
            return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question4.html', context)



# ##############################################################################
# question 9


def question9(request):
    basic_user_auth_check(request)
    details_checker_questions(request)
    
    context = {}
 
    if request.user.is_authenticated:


        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        try:
            token_of_user = request.session['token_ses']
            
            if 'question9' in request.session:
                del request.session['question9']
            else:
                pass

            if request.user:
                    # if token_of_user:
                        # prepare question
                        question9 = Questions.objects.filter(id = 9).first()
                        
                        context['question'] = question9
                        context['question_tag'] = 'Question 9'
                        context['question_tag_eng'] = 'Nine'
                        
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question9)
                        
                    
                        context['xlist'] = x_list
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                            question9Session = request.session['question9'] = []
                            
                            for i in list_checked:
                                check_answers = Answer.objects.filter(pk=int(i))
                                question9Session.append(str(check_answers.first())) 
                            
                            
                            
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
                    #     
                    # request.session.flush()
                    # logout(request)
                    # return redirect('login')           
            else:
                    messages.warning(request, 'User not verified')
        except:
            messages.warning(request, 'Error')
            return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question4.html', context)



# ##############################################################################
# question 10


def question10(request):
    basic_user_auth_check(request)
    details_checker_questions(request)
    
    context = {}
  
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        
        token_of_user = request.session['token_ses']
        try:
            if 'question10' in request.session:
                del request.session['question10']
            else:
                pass
            
        

            if request.user:
                    # if token_of_user:
                        # prepare question
                        question10 = Questions.objects.filter(id = 10).first()
                        
                        context['question'] = question10
                        context['question_tag'] = 'Question 10'
                        context['question_tag_eng'] = 'Ten'
                        
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question10)
                        
                    
                        context['xlist'] = x_list
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                            question10Session = request.session['question310'] = []
                            
                            
                        
                            
                            
                            for i in list_checked:
                                
                                check_answers = Answer.objects.filter(pk=int(i))
                                question10Session.append(str(check_answers.first())) 
                            
                            
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
                    #     
                    # request.session.flush()
                    # logout(request)
                    # return redirect('login')           
            else:
                    messages.warning(request, 'User not verified')
        except:
            messages.warning(request, 'Error')   
            return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question5.html', context)



# ##############################################################################
# question 11, 12, 13, 14


def questionCombined(request):
    basic_user_auth_check(request)
    details_checker_questions(request)
    
    context = {}
    
    
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        try:
        
            token_of_user = request.session['token_ses']
            
            if 'question11' in request.session:
                del request.session['question11']
            elif 'question12' in request.session:
                del request.session['question12']
            elif 'question13' in request.session:
                del request.session['question13']
            elif 'question14' in request.session:
                del request.session['question14']
            else:
                pass
            
        
            
        
            
            if token_of_user:
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
                            
                            question11Session = request.session['question11'] = []
                            question12Session = request.session['question12'] = []
                            question13Session = request.session['question13'] = []
                            question14Session = request.session['question14'] = []
                            
                            
                            for i in list_checked1:
                            
                                check_answers = Answer.objects.filter(pk=int(i))
                                question11Session.append(str(check_answers.first())) 
                            
                                for ans in check_answers:

                                    if ans.answer == 'Active systemic lupus erythematosus':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                        d.points +=3
                                        d.save()

                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                        d.points += 2
                                        d.save()

                                    elif ans.answer == 'Active heart failure':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                        d.points +=3
                                        d.save()
                                
                                    elif ans.answer == 'Previous thyroid pathology with current treatment':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                        d.points += 100
                                        d.save()
                                        
                                        
                                    elif ans.answer == 'Sickle cell anemia or thalassemia':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                        d.points +=3
                                        d.save()
                                        
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anaemia')
                                        d.points +=100
                                        d.save()
                                        # 
                                    elif ans.answer == 'Other hemoglobinopathy':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anaemia')
                                        d.points +=100
                                        d.save()
                                        
                                    elif ans.answer == 'Chronic hypertension (pre-pregnancy)':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                        d.points += 3
                                        d.save()
                                    elif ans.answer == 'Polycystic ovary syndrome':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                        d.points += 1
                                        d.save()
                                    elif ans.answer == 'Previous treatment with radioactive iodine':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                        d.points += 1
                                        d.save()
                                        
                                    elif ans.answer == 'Chronic kidney disease':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                        d.points += 2
                                        d.save()
                                    elif ans.answer == 'Active inflammatory bowel disease':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                        d.points +=3
                                        d.save()
                                        
                                    elif ans.answer == 'Chronic hepatitis C':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                        d.points +=1
                                        d.save()
                                        
                                    elif ans.answer == 'Previous thyroidectomy':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                        d.points += 1
                                        d.save()
                                        
                                    elif ans.answer == 'Active inflammatory polyarthritis':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                        d.points +=3
                                        d.save()
                                        
                                    elif ans.answer == 'Non-alcoholic fatty liver':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                        d.points +=1
                                        d.save()
                                    #  
                                    elif ans.answer == 'Goiter':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                        d.points +=1
                                        d.save()
                                        
                                    elif ans.answer == 'Type I diabetes mellitus':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                        d.points +=2
                                        d.save()
                                        
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thyroid disorder')
                                        d.points +=1
                                        d.save()
                                        
                                    elif ans.answer == 'Previous thyroiditis':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thyroid disorder ')
                                        d.points +=1
                                        d.save()
                                    elif ans.answer == 'Type 1 diabetes with renal involvement':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                        d.points +=1
                                        d.save()
                                    elif ans.answer == 'Type II diabetes':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                        d.points +=2
                                        d.save()

                                    elif ans.answer == 'Active nephrotic syndrome (renal pathology)':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = ' thrombosis')
                                        d.points +=3
                                        d.save()

                                    elif ans.answer == 'Obstetric/thrombotic antiphospholipid syndrome':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                        d.points +=2
                                        d.save()

                                    elif ans.answer == 'Subclinical hypothyroidism':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thyroid disorder ')
                                        d.points +=1
                                        d.save()

                                    elif ans.answer == 'Active cancer (others)':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                        d.points +=3
                                        d.save()
                                    
                                    elif ans.answer == 'Previous inflammatory pathology/surgery affecting iron absorption (celiac disease, current H. pylori infection, or inflammatory bowel disease)':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anemia')
                                        d.points +=1
                                        d.save()

                                    
                                    
                                        
                            for i in list_checked2:
                                
                                check_answers = Answer.objects.filter(pk=int(i))
                                question12Session.append(str(check_answers.first())) 
                                
                                
                                if ans.answer == 'Immobilization (wheelchair, paraplegia)':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Persistent positivity of antiphospholipid antibodies':
                                    d = Referal(
                                        token= request.session['token_ses'],
                                        patient= request.session['details'][2],
                                        answer = ans.answer,
                                        comment = 'high-risk Pregnancy team/Rheumatology'
                                    )
                                    d.save()
                                    
                                elif ans.answer == 'Insulin resistance or prediabetes':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'diabetes')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Interval between pregnancies < 1 year':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anemia')
                                    d.points +=1
                                    d.save()

                                                            
                                if ans.answer == 'Interval between pregnancies > 10 years)':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Positivity of antithyroid antibodies':
                                    pass
                                
                                elif ans.answer == 'Current intravenous drug use':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()

                                elif ans.answer == 'Palpable thick venous varices':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=1
                                    d.save()                            
                                elif ans.answer == 'Current smoker':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=1
                                    d.save()     
                                    
                                elif ans.answer == 'Preeclampsia in current pregnancy':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=1
                                    d.save()   
                                                            
                                                        
                                elif ans.answer == 'Hyperemesis gravidarum in current pregnancy':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thyroid disorder')
                                    d.points +=1
                                    d.save()                            
                                elif ans.answer == 'Currently on treatment with corticosteroids or antipsychotics':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'diabetes ')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Previous pregnancy with a baby weighing >4.5 kg':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'diabetes ')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'History of liver enzyme abnormalities with oral contraceptives':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'intrahepatic cholestasis')
                                    d.points +=1
                                    d.save()
                                
                                elif ans.answer == 'Previous intravenous iron therapy':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anemia')
                                    d.points +=1
                                    d.save()
                                elif ans.answer == 'Following a vegetarian or vegan diet':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anemia')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Recent history of significant bleeding':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anemia')
                                    d.points +=1
                                    d.save()

        
                                        
                            for i in list_checked4:
                                
                                check_answers = Answer.objects.filter(pk=int(i))
                                question14Session.append(str(check_answers.first())) 
                            
                                if ans.answer == 'thyroid disorder Familial autoimmune':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thyroid disease')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Preeclampsia':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Mother/sisters or daughters with intrahepatic cholestasis':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = ' intrahepatic cholestasis')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Deep vein thrombosis':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=1
                                    d.save()

                                                            
                                elif ans.answer == 'Mother/sisters or daughters with hyperemesis gravidarum':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Hyperemesis gravidarum')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Mother/sisters or daughters with diabetes mellitus':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'diabetes')
                                    d.points +=1
                                    d.save()   
                                
                                elif ans.answer == 'Familial genetic thrombophilia (including factor V Leiden, mutation of the prothrombin gene, protein C or S)':
                                
                                    d = Referal(
                                        token= request.session['token_ses'],
                                        patient= request.session['details'][2],
                                        answer = ans.answer,
                                        comment = 'Visit Hematology'
                                    )
                                    d.save

                                
                                                            
                            for i in list_checked3:
                                
                                check_answers = Answer.objects.filter(pk=int(i))
                                question13Session.append(str(check_answers.first())) 
                                
                                
                                if ans.answer == 'Preeclampsia or chronic arterial hypertension':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points +=2
                                    d.save()
                                    
                                elif ans.answer == 'Gestational diabetes':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'diabetes')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Hyperemesis gravidarum':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anemia')
                                    d.points +=1
                                    d.save()

                                                            
                                if ans.answer == 'Hypothyroidism/hyperthyroidism':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = ' thyroid disorder')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Anaemia':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'anaemia')
                                    d.points +=1
                                    d.save()
                                
                                elif ans.answer == 'Intrahepatic cholestasis':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'None of the above':
                                    pass
                                                            
                                elif ans.answer == 'I have not been pregnant':
                                    pass                  
                                
                                
                                
                                    request.session['questions_answered'] = [1,2,3,4,5,6,7,8,9, 10, 11, 13, 14]
                                    request.session.modified = True
                                    
                                                                        

                            return redirect('save_result_user')
                            # send question and answer to view
                    
                
                    # else:
                    #     messages.warning(request, 'Access denied')
                    #     
                    # request.session.flush()
                    # logout(request)
                    # return redirect('login')           
            else:
                    messages.warning(request, 'User not verified')
        except:
            messages.warning(request, 'Error')
            return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question6.html', context)


# ##############################################################################
# question 15


def question15(request):
    
    context = {}
    
    token_of_user = request.session['token_ses']
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        
        try:
        
            if 'question15' in request.session:
                del request.session['question15']
            else:
                pass
            
        

            if request.user:
                    # if token_of_user:
                        # prepare question
                        question15 = Questions.objects.filter(id = 15).first()
                        
                        context['question'] = question15
                        context['question_tag'] = 'Question 15'
                        context['question_tag_eng'] = 'Fifteen'
                        
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question15)
                        
                    
                        context['xlist'] = x_list
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                            question15Session = request.session['question15'] = []
                            
                            for i in list_checked:
                                check_answers = Answer.objects.filter(pk=int(i))
                                question15Session.append(str(check_answers.first()))    
                            
                            
                                for ans in check_answers:
                                
                                    if ans.answer == 'You have been diagnosed with a previous or current psychiatric disorder including schizophrenia, bipolar disorder, obsessive-compulsive disorder, or eating disorder (such as bulimia or anorexia), amon':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                        d.points +=100
                                        d.save()

                                

                                    elif ans.answer == 'You are currently undergoing psychiatric treatment with medication (including antidepressants, antipsychotics, mood stabilizers, stimulant medication or anxiety medication, among others).':
                                        
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                        d.points +=100
                                        d.save()

                                
                                    elif ans.answer == 'You have had previous suicide attempts.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                        d.points +=100
                                        d.save()


                                    elif ans.answer == 'You have a history of psychosis, depression, or anxiety (including previous pregnancies and postpartum).':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                        d.points += 1
                                        d.save()
                                    
                                    elif ans.answer == 'You have a family history (parents, siblings or children) of mental illness (including postpartum psychosis, bipolar disorder, anxiety or depression).':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                        d.points +=1
                                        d.save()

                                    elif ans.answer == 'You have problems living with your current partner.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                        d.points +=1
                                        d.save()

                                    
                                    elif ans.answer == 'You have current financial problems.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                        d.points +=1
                                        d.save()

                                    
                                    elif ans.answer == 'You have little or no family or friend support to rely on for the care of your baby.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                        d.points +=1
                                        d.save()

                                    
                                    elif ans.answer == 'The current pregnancy is unwanted.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                        d.points +=1
                                        d.save()

                                        
                                        
                                    request.session['questions_answered'] = [1,2,3,4,5,6,7,8,9, 10, 11, 13,14,15]
                                    request.session.modified = True
                                    
                                        
                                    

                            return redirect('question16')
                            # send question and answer to view
                    
                
                    # else:
                    #     messages.warning(request, 'Access denied')
                    #     
                    # request.session.flush()
                    # logout(request)
                    # return redirect('login')           
            else:
                    messages.warning(request, 'User not verified')
        except:
            messages.warning(request, 'Error')
            return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question5.html', context)




# ##############################################################################
# question 16


def question16(request):
    
    context = {}
    
    token_of_user = request.session['token_ses']
  
    if request.user.is_authenticated:

        try:
        
            if 'question16' in request.session:
                del request.session['question16']
            else:
                pass
    
            if request.user:
                    # if token_of_user:
                        # prepare question
                        question16 = Questions.objects.filter(id = 16).first()
                        
                        context['question'] = question16
                        context['question_tag'] = 'Question 16'
                        context['question_tag_eng'] = 'Sixteen'
                        
                        # get answers ans send form to frontend
                        
                        x_list = Answer.objects.filter(question=question16)
                        question16Session = request.session['question16'] = []
                        
                        context['xlist'] = x_list
                        if request.method =='POST':
                            
                            list_checked = request.POST.getlist('xlist_boxes')
                            question16Session = request.session['question16'] = []
                            
                            for i in list_checked:
                                check_answers = Answer.objects.filter(pk=int(i))
                                question16Session.append(str(check_answers.first())) 
                            
                            
                            for ans in check_answers:
                                
                                    if ans.answer == 'You have difficulty concentrating.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                        d.points +=1
                                        d.save()

                                

                                    elif ans.answer == 'You get easily angry or irritable.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                        d.points +=1
                                        d.save()

                                    elif ans.answer == 'You have difficulty sleeping at night.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                        d.points +=1
                                        d.save()
                                        
                                    elif ans.answer == 'You feel anxious or nervous.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                        d.points +=1
                                        d.save()
                                        
                                    elif ans.answer == "You can't stop repeatedly thinking about the same thing.":
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                        d.points +=1
                                        d.save()
                                    elif ans.answer == 'You are afraid that something bad will happen during your pregnancy.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                        d.points +=1
                                        d.save()
                                        
                                    elif ans.answer == 'You have constant negative thoughts.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Depression')
                                        d.points +=1
                                        d.save()
                                        
                                    elif ans.answer == "You feel guilty about the problems you're currently experiencing.":
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease ='Depression')
                                        d.points += 1
                                        d.save()
                                        
                                    elif ans.answer == 'Loss of interest in the people around you or everyday activities.':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease ='Depression')
                                    
                                        d.points +=1
                                        d.save()
                                        
                                    elif ans.answer == 'You feel sad, down or more easily prone to tears':
                                        d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Depression')
                                        d.points +=1
                                        d.save()
                                        
                                    request.session['questions_answered'] = [1,2,3,4,5,6,7,8,9, 10, 11, 13,14,15, 16]
                                    request.session.modified = True
                                    
                        

                            return redirect('save_result_user')
                            # send question and answer to view
                    
                
                    # else:
                    #     messages.warning(request, 'Access denied')
                    #     
                    # request.session.flush()
                    # logout(request)
                    # return redirect('login')           
            else:
                    messages.warning(request, 'User not verified')
                    return redirect('login')
        except:
            messages.warning(request, 'Error')
            return redirect('login')     
    else:
        messages.warning(request, 'Authentication required')
        return redirect('login')
    return render(request, 'questions/question4.html', context)



@login_required(login_url='login')
def save_result_user(request):
    
    # get all sessions 
    

    token = request.session['token_ses']
    
    
    
    
    # get all diseases
    diseases = Disease.objects.filter(user_diagnosed = token)
    for i in diseases:
        
        d = Disease_result(
            disease = i.disease,
            point = int(i.points),
            mom_full_name= request.session['details'][2],
            token = request.session['token_ses'],
            )
        
        d.save()


    #  store needed data
    
    
    result = Result_owner(
    full_name =  request.session['details'][2],
    token = request.session['token_ses'],
    auth_password = request.session['auth_password'],
    app_password = request.session['app_password'],
    browser = request.session['details'][0],
    device = request.session['details'][1],
    user_profile = request.session['user_profile'],
    age = request.session['age'],  
    email =  request.session['email'],
    
    )
    
    # save  
    result.save()
    

    if 'language' in request.session:
        if request.session['language'] == 'spanish':
            return redirect('success_page_spanish')
    
        elif request.session['language'] == 'english':
            return redirect('success_page')
            
            
    else:
        messages.warning(request, 'Login required')
        return redirect('login')
    
# ####################################################################
#generate PDF

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


data = {
	"company": "RFP-Algorithm",
	"address": "United Kingdom",
	"website": "rfpalgorithm.com",
	}

#Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {}
            # get all results for current user 
            disease = Disease_result.objects.filter(token=request.session['token_ses'])
            refers = Referal.objects.filter(token=request.session['token_ses'])
            datas = Result_owner.objects.filter(token=request.session['token_ses'])
            bmi= BMI.objects.filter(token=request.session['token_ses'])
            context['mom_data'] = datas
            
            # #####################################################################
            for i in disease:
        ####################################################### 
                
                    if i.disease == 'preeclampsia':
                      
                        if int(i.point) >= 2:    
                           
                            context['preeclampsia']  = 'yes'
                            
                        elif int(i.point) <= 1:    
                               
                            context['preeclampsia_b']  = 'yes'  
                          
        ####################################################### 
                    elif i.disease == 'thrombosis':
                        if int(i.point) >= 100:    
                         
                            
                            context['thrombosis']  = 'yes'
                                     
                        elif int(i.point) >=4 :
                     
                            
                            context['thrombosis_b']  = 'yes'
                            
                        elif int(i.point) == 3:
                      
                            context['thrombosis_c']  = 'yes'
                        
                        
                        elif int(i.point) <= 2:
                         
                            
                            context['thrombosis_d']  = 'yes'
                        
                        
        ####################################################### 
                             
                    elif i.disease == 'Diabetes Mellitus':
                    
                        if int(i.point) >= 1:    
                            context['gestation']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['gestation_b']  = 'yes'
   
#    ##################################################
   
                    elif i.disease == 'Thyroid disorders':
                    
                        if int(i.point) >= 1:    
                            context['thyroid']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['thyroid_b']  = 'yes'
   
#    ##################################################
                    elif i.disease == 'Anaemia':
                    
                        if int(i.point) >= 1:    
                            context['anemia']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['anemia_b']  = 'yes'
#    ##################################################
   
   
                    elif i.disease == 'Hyperemesis gravidarum':
                    
                        if int(i.point) >= 1:    
                            context['hyperemesis']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['hyperemesis_b']  = 'yes'
   
      
#    ##################################################
   
                    elif i.disease == 'Intrahepatic cholestasis':
                    
                        if int(i.point) >= 1:    
                            context['intrahepatic']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['intrahepatic_b']  = 'yes'
   
   
        
        

   
   
   
   
        ####################################################### 
          

            
            
            
            pdf = render_to_pdf('pages/generate_pdf.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
        
        else:
            return redirect('login')




#Automatically downloads to PDF file

class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        context = {}
        disease = Disease.objects.filter(token=request.session['token_ses'])
        refers = Referal.objects.filter(token=request.session['token_ses'])
        datas = Result_owner.objects.filter(token=request.session['token_ses'])
        for i in datas:
            print(i)
       
        bmi= BMI.objects.filter(token=request.session['token_ses'])
        context['mom_data'] = datas
        
        # #####################################################################
  
        
        for i in disease:
        ####################################################### 
                
                    if i.disease == 'preeclampsia':
                      
                        if int(i.point) >= 2:    
                           
                            context['preeclampsia']  = 'yes'
                            
                        elif int(i.point) <= 1:    
                               
                            context['preeclampsia_b']  = 'yes'  
                          
        ####################################################### 
                    elif i.disease == 'thrombosis':
                        if int(i.point) >= 100:    
                         
                            
                            context['thrombosis']  = 'yes'
                                     
                        elif int(i.point) >=4 :
                     
                            
                            context['thrombosis_b']  = 'yes'
                            
                        elif int(i.point) == 3:
                      
                            context['thrombosis_c']  = 'yes'
                        
                        
                        elif int(i.point) <= 2:
                         
                            
                            context['thrombosis_d']  = 'yes'
                        
                        
        ####################################################### 
                             
                    elif i.disease == 'Diabetes Mellitus':
                    
                        if int(i.point) >= 1:    
                            context['gestation']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['gestation_b']  = 'yes'
   
#    ##################################################
   
                    elif i.disease == 'Thyroid disorders':
                    
                        if int(i.point) >= 1:    
                            context['thyroid']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['thyroid_b']  = 'yes'
   
#    ##################################################
                    elif i.disease == 'Anaemia':
                    
                        if int(i.point) >= 1:    
                            context['anemia']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['anemia_b']  = 'yes'
#    ##################################################
   
   
                    elif i.disease == 'Hyperemesis gravidarum':
                    
                        if int(i.point) >= 1:    
                            context['hyperemesis']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['hyperemesis_b']  = 'yes'
   
      
#    ##################################################
   
                    elif i.disease == 'Intrahepatic cholestasis':
                    
                        if int(i.point) >= 1:    
                            context['intrahepatic']  = 'yes'
                    

                        elif int(i.point) == 0:
                            context['intrahepatic_b']  = 'yes'
   
   
        
        
        
        
        
        
        
        context['refer'] = refers
        context['disease'] = disease
        context['mom_data'] = Result_owner.objects.filter(token=request.session['token_ses'])
        pdf = render_to_pdf('pages/generate_pdf.html', context)
        response = HttpResponse(pdf, content_type='application/pdf')
        
        filename = "Result_RFP-Algorithm_%s.pdf" %("12341231")
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response






# after success of test show page
@login_required(login_url="login")
def success_page(request):
    # request.session.set_expiry(240)
    context = {}
    # check requirements to comfirm user finished test
    # x = ['question1', 'question2', 'question3','question4', 'question5', 'question6''question7', 'question7', 'question8''question9', 'question10', 'question11', 'question12', 'question13', 'question14''question15', 'question16']

    # for i in x:
    #     if i in request.session:
    #         pass 
    #     else:
    #         messages.warning(request, 'You didnt complete your questions')
    #         return redirect(i)
    
    
    
    # greet user and give option to download 
    user_full_name = request.session['details'][2]
    context['full_name'] = user_full_name
    return render(request, 'pages/success_page.html', context)




def dashboard_result_view(request):
    context = {}
    disease = Result_owner.objects.all()
           
    # segmented data
            
    context['total_patient'] = Result_owner.objects.count()
    context['test_taken'] = Result_owner.objects.count()
    context['hospital'] = RegisterClient.objects.count()
    context['access'] = PasswordStorage.objects.count()
            
    context['disease'] = disease
    
    return render(request, 'admin_pages/result.html', context)



# choose language 

# @login_required('login_url="login')

def  choose_language(request):
    
    if request.user.is_authenticated:
        logout(request)
        return redirect('language')
    else:
        pass
    
    if 'language' in request.session:
        del request.session['language']
        request.session.modified = True
        
    else:
        pass
    
    messages.info(request, "Choose a language ")
    return render(request, 'pages/language.html')
    
    
    
def choose_language_spanish(request):
    
    
    return redirect('loginspanish')
    
    

    
def choose_language_english(request):
    
    return redirect('login')
    
    

# contact page
def contact(request):
    context = {}
    if request.method == 'POST':
        names = request.POST['name']
        emails = request.POST['email']
        messages_ = request.POST['message']
        
        contact = ContactSubmission(
            name = names,
            email= emails,
            message= messages_ 
        )

        contact.save()
        messages.success(request, 'Thank you, We will reach out shortly')
        return redirect('language')

            
    else:
        pass 
    
    return render(request, 'pages/contact.html', context)
    
    
    