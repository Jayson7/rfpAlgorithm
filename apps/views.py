# all views here are fort the main page functions 


from django.shortcuts import render, redirect
from authenticator.models import UserLoginToken
from .models import *
from .questionForm import *
# Create your views here.

def choose_test(request):
    pass 


# 404 here 
def page_not_found(request):
    pass 


def question_controller(request):
    user = request.user 
    
    
    # check authentication 
    
    # check verification status 
    
    # controll questions 
    

# question 1

def question1(request):
    context = {}
    # if request.user.is_authenticated:
    user = request.user 
        # loctate user on token 
    try:
            # token_of_user = UserLoginToken.objects.filter(username=user).first()
            
                # prepare question
        question1 = Questions.objects.filter(id = 1).first()
        
        print(question1.question) 
        # get answers ans send form to frontend
        # form = Question1Form()

        # send question and answer to view
        context['question'] = question1
                
    except:
        return redirect('login')     
    # else:
    #     return redirect('login')
    return render(request, 'questions/question1.html', context)



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

