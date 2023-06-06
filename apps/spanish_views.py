from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import datetime 
from authenticator.models import *
from .models import *
from django.http import HttpResponse
from authenticator.views import basic_user_auth_check_spanish, details_checker_questions
from django.views.decorators.csrf import csrf_exempt


# question 1
@csrf_exempt
def question1Spanish(request):
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    context = {}

    if request.user.is_authenticated:
        
        try:
            # locate user on token 
            token_of_user = request.session['token_ses']
        
            if token_of_user:
                        # prepare question
                    question1 = QuestionsSpanish.objects.filter(id = 1).first()
                            
                            # get answers ans send form to frontend
                   
                    if request.method =='POST':
                                    age = request.POST['age']
                                # convert to integer
                                    try:
                                      x =  int(age)
                                    except:
                                        messages.warning(request, 'Entrada inválida')
                                        return redirect('question1s')
                        
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
                                    request.session['q1s'] = [x]
                                    request.session['questions_answered_spanish'] = [1]
                                    request.session.modified = True
                                    
                                        
                                    return redirect('question2s')
                       
                                    
                            # send question and answer to view
                    context['question'] = question1
              
            else:
                    messages.warning(request, 'Acceso denegado')
                    return redirect('loginspanish')           

        except:
            messages.warning(request, 'Error')
            return redirect('loginspanish')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspansih')
    return render(request, 'questions/spanish/question1spanish.html', context)


# question 2

def question2Spanish(request):
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    context = {}
    
    
    if request.user.is_authenticated:

        try: 
            user = request.user 
            token_of_user = request.session['token_ses']
            # verify if user answered question 1
    
            if token_of_user:
    
                            # prepare question
                        question2 = QuestionsSpanish.objects.filter(id = 2).first()
                                
        
                        # get answers ans send form to frontend
            
                        if request.method =='POST':
                                        height = request.POST['height']
                                        weight = request.POST['weight']
    
                                        # try coversions 
                                        try:
                                            height  = float(height)
                                            weight = float(weight)
                                            
                                        except:
                                            messages.warning(request, 'Se requiere una entrada válida')
                                            return redirect('loginspanish')  
                                        # add up missing form fields and calculate BMI
                                        
                                    
                                        
                                        
                                        # calculate BMI
                                        
                                        height_pow = height ** 2
                                        bmi = weight / height_pow
                                        
                                        if bmi < 18.5:
                                            BMI = 'Under Weight'
                                        elif bmi >= 18.5 and bmi <= 24.9:
                                            BMI = 'Mormal'
                                        elif bmi >= 25 and bmi <= 29.9:
                                            BMI = 'Over Weight'
                                        elif bmi >= 30 and bmi <= 34.9:
                                            BMI = 'Obesity (Class I)'                   
                                        elif bmi >= 35 and bmi <= 39.9:
                                            BMI = 'Obesity (Class II)'                                       
                                        elif bmi >= 40:
                                            BMI = 'Obesity (Extreme Obesity)'    
                                        
                    
                                        request.session['q2s'] = [BMI, height, weight]
                                        
                                        request.session['questions_answered_spanish'] = [1,2]
                                        request.session.modified = True
                                            
                                        return redirect('question3s')
                    
                                        
                                # send question and answer to view
                        context['question'] = question2
                    
                        
            else:
                    messages.warning(request, 'Usuario no verificada')
            # except:
            #     messages.warning(request, 'Error')
            #     return redirect('login')     
            
        except:
            messages.warning(request, 'Error de verificación de usuario') 
            return redirect('loginspanish')
        
    else:
            messages.warning(request, 'Autenticacion requerida')
            return redirect('loginspanish')
    return render(request, 'questions/spanish/question2spanish.html', context)



# ##############################################################################
# question 3


def question3Spanish(request):
    
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    context = {}
   
    if request.user.is_authenticated:
        user = request.user 
        token_of_user = request.session['token_ses']

        try:
            if token_of_user:

                    question3 = QuestionsSpanish.objects.filter(id = 3).first()
          
                    context['question'] = question3
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question3)
                   
                    context['xlist'] = x_list
                    
                    if 'question3s' in request.session:
                        del request.session['question3s']
                    else:
                        pass 
                  
                            
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        
                        
                        question3Session = request.session['question3s'] = []
                        
                        for i in list_checked:
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question3Session.append(str(check_answers.first())) 
                     
                           
                          
                           
                            for ans in check_answers:
                                if ans.answer == 'Asiático':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points += 1
                                    d.save()
                                    
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                    d.points += 1
                                    d.save()
                                   
                                   
                                elif ans.answer == 'Raza negra':
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
                                    
                                elif ans.answer == 'Oriente Medio/árabe':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                    d.points += 1
                                    d.save()
                                elif ans.answer == 'Otro':
                                    pass
                                elif ans.answer == 'Nativo americano':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                    d.points += 1
                                    d.save()
                                   
                                elif ans.answer == 'Raza blanca':
                                    pass 
                                
                                    
                                    
                                   
                                request.session['questions_answered_spanish'] = [1,2,3]
                                request.session.modified = True
                                
                        return redirect('question4s')
                        # send question and answer to view
                
               
                # else:
                    # messages.warning(request, 'Acceso denegado')
                    # return redirect('login')           
            else:
                messages.warning(request, 'Usuario no verificado')
        except:
            messages.warning(request, 'Error')
            return redirect('loginspanish')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question3spanish.html', context)




# ##############################################################################
# question 4


def question4Spanish(request):
        
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    
    context = {}
 
    if request.user.is_authenticated:

        user = request.user 
        token_of_user = request.session['token_ses']
      
        if token_of_user:
      
                    # prepare question
                    question4 = QuestionsSpanish.objects.filter(id = 4).first()
                    
                    context['question'] = question4
                    context['question_tag'] = 'Pregunta 4'
                    context['question_tag_eng'] = 'cuatro'
                    
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question4)
                    
                    if 'question4s' in request.session:
                        del request.session['question4s']
                    else:
                        pass
         
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                       
                        question4Session = request.session['question4s'] = []
                        
                        for i in list_checked:
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question4Session.append(str(check_answers.first())) 
                           
                            for ans in check_answers:
                               
                                if ans.answer == 'Primer embarazo ó pérdida gestacional menor 20 semanas':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Hyperemesis gravidarum')
                                    d.points +=1
                                    d.save()

                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 1
                                    d.save()

                                elif ans.answer == '2 partos':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points+= 1
                                    d.save()
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anaemia')
                                    d.points += 1
                                    d.save()
                               
                                elif ans.answer == '3 ó más partos':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()

                                else:
                                    pass
                                
                                
                                request.session['questions_answered_spanish'] = [1,2,3,4]
                                request.session.modified = True
                                # print(request.session['questions_answered_spanish'])
                                    
                                   

                        return redirect('question5s')
                        # send question and answer to view
                
                      
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question4spanish.html', context)





# ##############################################################################
# question 5


def question5Spanish(request):

    context = {}
    
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
   
    
    if request.user.is_authenticated:

        token_of_user = request.session['token_ses']
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        
        if 'question5s' in request.session:
            del request.session['question5s']
        else:
                pass
         
     
        
      
        
        if token_of_user:
      
                    # prepare question
                    question5 = QuestionsSpanish.objects.filter(id = 5).first()
                    
                    context['question'] = question5
                    context['question_tag'] = 'Pregunta 5'
                    context['question_tag_eng'] = 'cinco'
                    
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question5)
                    
                  
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        question5Session = request.session['question5s'] = []
                        
                        for i in list_checked:
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question5Session.append(str(check_answers.first())) 
                           
                           
                            for ans in check_answers:
                               
                                if ans.answer == 'No':
                                    pass
                                elif ans.answer == 'Sí':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points+= 1
                                    d.save()
                           
                                elif ans.answer == 'No estoy embarazada actualmente':
                                    pass
                                
                                    
                                request.session['questions_answered_spanish'] = [1,2,3,4,5]
                                request.session.modified = True
                      
                        return redirect('question6s')
                        # send question and answer to view
                
                      
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question4spanish.html', context)



# ##############################################################################
# question 6


def question6Spanish(request):
    
    context = {}

    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    
    
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        token_of_user = request.session['token_ses']
        
        if 'question6s' in request.session:
            del request.session['question6s']
        else:
            pass
         
     
        

        if token_of_user:
        # if request.user:
                # if token_of_user:
                    # prepare question
                    question6 = QuestionsSpanish.objects.filter(id = 6).first()
                    
                    context['question'] = question6
                    context['question_tag'] = 'Pregunta 6'
                    context['question_tag_eng'] = 'Seis'
                    
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question6)
                    
                  
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        question6Session = request.session['question6s'] = []
                        
                        for i in list_checked:
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question6Session.append(str(check_answers.first())) 
                           
                           
                            for ans in check_answers:
                               
                                if ans.answer == 'Sí':
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
                                elif ans.answer == 'No' or ans.answer == 'No estoy embarazada actualmente':
                                    pass 
                                
                                
                                request.session['questions_answered_spanish'] = [1,2,3,4,5,6]
                                request.session.modified = True
                      

                        return redirect('question7s')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Acceso denegado')
                #     return redirect('login')           
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question4spanish.html', context)




# ###############################################################################################
# question 7


def question7Spanish(request):
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    
    context = {}

    if request.user.is_authenticated:

        user = request.user 
        # locate user on token 

        full_name = request.session['details'][2]
        # try:
        if 'question7s' in request.session:
            del request.session['question7s']
        else:
            pass
         
            token_of_user = request.session['token_ses']
        
        
        if request.user:
                # if token_of_user:
                    # prepare question
                    question7 = QuestionsSpanish.objects.filter(id = 7).first()
                    
                    context['question'] = question7
                    context['question_tag'] = 'Pregunta 7'
                    context['question_tag_eng'] = 'Siete'
                    
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question7)
                    
                  
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        question7Session = request.session['question7s'] = []
                        
                        for i in list_checked:
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
        
                            question7Session.append(str(check_answers.first())) 
                           
                           
                            for ans in check_answers:
                               
                                if ans.answer == 'Sí, he sido diagnosticada de trombosis venosa profunda Y estoy actualmente en tratamiento anticoagulante.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 100 
                                    d.save()
                                
                                
                                elif ans.answer == 'No, no estoy en tratamiento anticoagulante para una trombosis venosa profunda previa.':
                                    pass
           
                                request.session['questions_answered_spanish'] = [1,2,3,4,5,6,7]
                                request.session.modified = True

                        return redirect('question8s')
                        # send question and answer to view

                # else:
                #     messages.warning(request, 'Acceso denegado')
                #     return redirect('login')           
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question4spanish.html', context)




# ##############################################################################

# question 8


def question8Spanish(request):
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    
    context = {}
    
    
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        
        token_of_user = request.session['token_ses']
        if 'question8s' in request.session:
            del request.session['question8s']
        else:
            pass
         

        
        if request.user:
                # if token_of_user:
                    # prepare question
                    question8 = QuestionsSpanish.objects.filter(id = 8).first()
                    
                    context['question'] = question8
                    context['question_tag'] = 'Pregunta 8'
                    context['question_tag_eng'] = 'Ocho'
                    
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question8)
                    
                  
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        question8Session = request.session['question8'] = []
                        
                        for i in list_checked:
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question8Session.append(str(check_answers.first())) 
                           
                           
                            for ans in check_answers:
                               
                                if ans.answer == 'Sí, he sido diagnosticada de deficiencia de antitrombina ó síndrome antifosfolípido trombótico.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 100 
                                    d.save()


                                elif ans.answer == 'No, no he sido diagnosticada de deficiencia de antitrombina ó síndrome antifosfolípido trombótico.':
                                    pass
                            
                                    
                                    
                        request.session['questions_answered_spanish'] = [1,2,3,4,5,6,7,8]
                        request.session.modified = True

                        return redirect('question9s')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Acceso denegado')
                #     return redirect('login')           
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question4spanish.html', context)



# ##############################################################################
# question 9


def question9Spanish(request):
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    
    context = {}
 
    if request.user.is_authenticated:


        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        token_of_user = request.session['token_ses']
        
        if 'question9s' in request.session:
            del request.session['question9s']
        else:
            pass

        if request.user:
                # if token_of_user:
                    # prepare question
                    question9 = QuestionsSpanish.objects.filter(id = 9).first()
                    
                    context['question'] = question9
                    context['question_tag'] = 'Pregunta 9'
                    context['question_tag_eng'] = 'Nueve'
                    
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question9)
                    
                  
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        question9Session = request.session['question9'] = []
                        
                        for i in list_checked:
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question9Session.append(str(check_answers.first())) 
                           
                           
                           
                            for ans in check_answers:
                               
                                if ans.answer == 'Sí, fui diagnosticada de trombosis venosa profunda Y NO estoy actualmente en tratamiento anticoagulante (La causa de la trombosis fue una cirugía reciente)':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()


                                elif ans.answer == 'Sí, fui diagnosticada de trombosis venosa profunda Y NO estoy actualmente en tratamiento anticoagulante (La causa de la trombosis es desconocida u otra diferente a una cirugía)':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 4
                                    d.save()

                               
                                elif ans.answer == 'No, no he tenido nunca una trombosis venosa profunda.':
                                    pass 
             
                                
                                request.session['questions_answered_spanish'] = [1,2,3,4,5,6,7,8,9]
                                request.session.modified = True
                      
    

                        return redirect('question10s')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Acceso denegado')
                #     return redirect('login')           
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question4spanish.html', context)


# ##############################################################################
# question 10


def question10Spanish(request):
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    
    context = {}
  
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        
        token_of_user = request.session['token_ses']
        
        # try:
        if 'question10s' in request.session:
            del request.session['question10s']
        else:
            pass
        
        if request.user:
                # if token_of_user:
                    # prepare question
                    question10 = QuestionsSpanish.objects.filter(id = 10).first()
                    
                    context['question'] = question10
                    context['question_tag'] = 'Pregunta 10'
                    context['question_tag_eng'] = 'Diez'
                    
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question10)
                    
                  
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        question10Session = request.session['question310'] = []
                        
                        for i in list_checked:
                            
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question10Session.append(str(check_answers.first())) 
                           
                            for ans in check_answers:
                               
                                if ans.answer == 'Factor homocigoto V Leiden':
                                    
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()

                                elif ans.answer == 'Factor heterocigoto V Leiden':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()
                               
                                elif ans.answer == 'Mutación homocigota del gen de la protrombina':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()                                
                                elif ans.answer == 'Mutación heterocigota del gen de la protrombina':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()                                
                                elif ans.answer == 'Deficiencia de proteína C':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()
                                elif ans.answer == 'Deficiencia de proteína S':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()
                                elif ans.answer == 'Síndrome antifosfolípido obstétrico':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()
                                elif ans.answer == 'Combinación del factor V heterocigoto de Leiden y mutación del gen de la protrombina heterocigota':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 3
                                    d.save()
                                    
                                request.session['questions_answered_spanish'] = [1,2,3,4,5,6,7,8,9, 10]
                                request.session.modified = True
                       
                        return redirect('questionCss')
                        # send question and answer to view
              
                # else:
                #     messages.warning(request, 'Acceso denegado')
                #     return redirect('login')           
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question5spanish.html', context)



# ##############################################################################
# question 11, 12, 13, 14



def questionCombinedSpanish(request):
    basic_user_auth_check_spanish(request)
    details_checker_questions(request)
    
    context = {}
    
    if request.user.is_authenticated:
        
        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        
        token_of_user = request.session['token_ses']
        
        if 'question11s' in request.session:
            del request.session['question11s']
        elif 'question12s' in request.session:
            del request.session['question12s']
        elif 'question13s' in request.session:
            del request.session['question13s']
        elif 'question14' in request.session:
            del request.session['question14s']
        else:
            pass
         
     
        if token_of_user:
        # if request.user:
                # if token_of_user:
                    # prepare question
                    question11 = QuestionsSpanish.objects.filter(id = 11).first()
                    question12 = QuestionsSpanish.objects.filter(id = 12).first()
                    question13 = QuestionsSpanish.objects.filter(id = 13).first()
                    question14 = QuestionsSpanish.objects.filter(id = 14).first()
                    
                    context['question1'] = question11
                    context['question2'] = question12
                    context['question3'] = question13
                    context['question4'] = question14
                    context['question_tag'] = 'Pregunta 11, 12, 13 & 14'
                    context['question_tag_eng'] = 'Once, , Doce. Trece y Catorce'
                    
                    # get answers ans send form to frontend
                    
                    x_list1 = AnswerSpanish.objects.filter(question=question11)
                    x_list2 = AnswerSpanish.objects.filter(question=question12)
                    x_list3 = AnswerSpanish.objects.filter(question=question13)
                    x_list4 = AnswerSpanish.objects.filter(question=question14)
 
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
                           
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question11Session.append(str(check_answers.first())) 
                           
                            for ans in check_answers:

                                if ans.answer == 'Lupus eritematoso sistémico activo ':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()

                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 2
                                    d.save()

                                elif ans.answer == 'Insuficiencia cardíaca activa':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                               
                                elif ans.answer == 'Patología tiroidea previa con tratamiento actual':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                    d.points += 100
                                    d.save()
                                    
                                    
                                elif ans.answer == 'Anemia falciformes o Talasemia':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                                    
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anaemia')
                                    d.points +=100
                                    d.save()
                                    # 
                                elif ans.answer == 'Otra hemoglobinopatía':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anaemia')
                                    d.points +=100
                                    d.save()
                                    
                                elif ans.answer == 'Hipertensión arterial crónica (pre-embarazo)':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 3
                                    d.save()
                                elif ans.answer == 'Síndrome de ovarios poliquísticos':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Diabetes Mellitus')
                                    d.points += 1
                                    d.save()
                                elif ans.answer == 'Tratamiento previo con yodo radioactivo':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                    d.points += 1
                                    d.save()
                                    
                                elif ans.answer == 'Enfermedad renal crónica':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points += 2
                                    d.save()
                                elif ans.answer == 'Enfermedad inflamatoria intestinal activa':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                                    
                                elif ans.answer == 'Hepatitis C crónica':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Tiroiditis previa':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                    d.points += 1
                                    d.save()
                                    
                                elif ans.answer == 'Poliartritis inflamatoria activa':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                                    
                                elif ans.answer == 'Hígado graso no-alcohólico':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points +=1
                                    d.save()
                                 #  
                                elif ans.answer == 'Bocio':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Thyroid disorders')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Diabetes Mellitus tipo I':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points +=2
                                    d.save()
                                    
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disorder')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Patología inflamatoria/cirugía previa que afecta absorción del hierro (celiaquía, infección':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disorder ')
                                    d.points +=1
                                    d.save()
                                elif ans.answer == ' Diabetes tipo 1 con afectación renal':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                    d.points +=1
                                    d.save()
                                elif ans.answer == 'Diabetes Mellitus tipo 2':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points +=2
                                    d.save()

                                elif ans.answer == 'Síndrome nefrótico (patología renal) activo':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = ' thrombosis')
                                    d.points +=3
                                    d.save()

                                elif ans.answer == 'Síndrome antifosfolípido obstétrico/trombótico':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                    d.points +=2
                                    d.save()

                                elif ans.answer == 'Hipotiroidismo subclínico':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disorder ')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Cáncer activo (especificar)':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points +=3
                                    d.save()
                                
                                elif ans.answer == 'Patología inflamatoria/cirugía previa que afecta absorción del hierro (celiaquía, infección actual H Pilori ó enfermedad inflamatoria intestinal)':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                    d.points +=1
                                    d.save()

                                
                                
                                    
                        for i in list_checked2:
                            
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question12Session.append(str(check_answers.first())) 
                            
                            
                            if ans.answer == 'Inmovilidad (Silla de ruedas, paraplejia)':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Positividad persistente de anticuerpos antifosfolípidos':
                                d = Referal(
                                    token= request.session['token_ses'],
                                    patient= request.session['details'][2],
                                    answer = ans.answer,
                                    comment = 'high-risk Pregnancy team/Rheumatology'
                                )
                                d.save()
                                
                            elif ans.answer == 'Resistencia a la insulina ó prediabetes':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Intervalo entre embarazos < 1 año':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()

                                                        
                            if ans.answer == 'Intervalo entre embarazos > 10 años':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Positividad de anticuerpos antitiroideos':
                                pass
                             
                            elif ans.answer == 'Usuaria de drogas endovenosas actual':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=3
                                d.save()

                            elif ans.answer == 'Varices venosas gruesas palpables':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()                            
                            elif ans.answer == 'Fumadora actual':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()     
                                
                            elif ans.answer == 'Preeclampsia en el embarazo actual':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()   
                                                         
                                                     
                            elif ans.answer == 'Hiperémesis gravídica en el embarazo actual':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disorder')
                                d.points +=1
                                d.save()                            
                            elif ans.answer == 'En tratamiento actual con corticoides ó antipsicóticos':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes ')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Embarazo previo en el cual su hijo pesó >4,5 kg':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes ')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Historia de alteración de enzimas del hígado con anticonceptivos orales':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'intrahepatic cholestasis')
                                d.points +=1
                                d.save()
                            
                            elif ans.answer == 'Has precisado de tratamiento endovenoso con hierro previo.':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()
                            elif ans.answer == 'Sigues una dieta vegetariana o vegana':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()
                                
                            elif ans.answer == 'Historia reciente de sangrado importante':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()

     
                                    
                        for i in list_checked4:
                            
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question14Session.append(str(check_answers.first())) 
                           
                            if ans.answer == 'Trastorno tiroideo autoinmune familiar':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thyroid disease')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Preeclampsia':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()
                                
                            elif ans.answer == 'Trombofilia genética (incluyendo factor V Leiden, mutación del gen de la protrombina, proteína C o S) familiar':
                                pass 
                                # refer
                   
                            elif ans.answer == 'Madre/hermanas ó hijas con colestasis intrahepática':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = ' intrahepatic cholestasis')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Trombosis venosa profunda':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                d.points +=1
                                d.save()

                                                        
                            elif ans.answer == 'Madre/hermanas ó hijas con hiperémesis gravídica':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Hyperemesis gravidarum')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Madre/hermanas ó hijas con diabetes mellitus':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes')
                                d.points +=1
                                d.save()

                                                    
                        for i in list_checked3:
                            
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question13Session.append(str(check_answers.first())) 
                            
                            if ans.answer == 'Preeclampsia o hipertensión arterial crónica':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'preeclampsia')
                                d.points +=2
                                d.save()
                                
                            elif ans.answer == 'Diabetes gestacional ':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'diabetes')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Hiperémesis gravídica ':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Anemia')
                                d.points +=1
                                d.save()

                                                        
                            elif ans.answer == 'Hipotiroidismo / hipertiroidismo':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = ' thyroid disorder')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Anemia':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'anaemia')
                                d.points +=1
                                d.save()
                             
                            elif ans.answer == 'Colestasis intrahepática':
                                d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'Intrahepatic cholestasis')
                                d.points +=1
                                d.save()

                            elif ans.answer == 'Ninguno de los anteriores':
                                pass
                                                         
                            elif ans.answer == 'No he estado embarazada previamente':
                                pass                  
                     
                            
                                request.session['questions_answered_spanish'] = [1,2,3,4,5,6,7,8,9, 10, 11, 13, 14]
                                request.session.modified = True
                                
                                                                       

                        return redirect('question15s')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Acceso denegado')
                #     return redirect('login')           
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question6spanish.html', context)


# ##############################################################################
# question 15


def question15Spanish(request):
    
    context = {}
    
    token_of_user = request.session['token_ses']
    
    if request.user.is_authenticated:

        
        user = request.user 
            # locate user on token 
            
        full_name = request.session['details'][2]
        # try:
        
        if 'question15s' in request.session:
            del request.session['question15s']
        else:
            pass
         
     

        if request.user:
                # if token_of_user:
                    # prepare question
                    question15 = QuestionsSpanish.objects.filter(id = 15).first()
                    
                    context['question'] = question15
                    context['question_tag'] = 'Pregunta 15'
                    context['question_tag_eng'] = 'quince'
                    
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question15)
                    
                  
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        question15Session = request.session['question15'] = []
                        
                        for i in list_checked:
                            check_answers = AnswerSpanish.objects.filter(pk=int(i))
                            question15Session.append(str(check_answers.first()))    
                           
                           
                            for ans in check_answers:
                               
                                if ans.answer == 'Has sido diagnosticada de patología psiquiátrica previa ó actual incluyendo esquizofrenia, trastorno bipolar, trastorno obsesivo compulsivo ó trastorno alimentario (como bulimia o anorexia), entre otros':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                    d.points +=100
                                    d.save()

                               

                                elif ans.answer == 'Estás en tratamiento psiquiátrico actual con fármacos (incluyendo antidepresivos, antipsicóticos, estabilizantes del humor, medicamentos estimulantes o medicación para ansiedad, entre otras)':
                                    
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                    d.points +=100
                                    d.save()

                               
                                elif ans.answer == 'Has presentado intento(s) de suicidio previo':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                    d.points +=100
                                    d.save()


                                elif ans.answer == 'Tienes una historia previa de psicosis, depresión o ansiedad (incluyendo embarazos previos y postparto)':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'thrombosis')
                                    d.points += 1
                                    d.save()
                                
                                elif ans.answer == 'Tienes historia familiar (padres, herman@s o hij@s) de patología mental (incluyendo psicosis postparto, trastorno bipolar, ansiedad ó depresión) ':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Tienes problemas de convivencia con su pareja actual':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                    d.points +=1
                                    d.save()

                                
                                elif ans.answer == 'Tienes problemas económicos actuales':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                    d.points +=1
                                    d.save()

                                
                                elif ans.answer == 'Tienes escaso o ningún apoyo familiar ó de amistades en los que apoyarse para el cuidado de tu bebé':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                    d.points +=1
                                    d.save()

                                
                                elif ans.answer == 'Embarazo actual no deseado.':
                                    d = Disease.objects.filter(user_diagnosed=token_of_user, disease = 'pregnancy wellbeing')
                                    d.points +=1
                                    d.save()

                                    
                                    
                                request.session['questions_answered_spanish'] = [1,2,3,4,5,6,7,8,9, 10, 11, 13,14,15]
                                request.session.modified = True
                                
                                    
                                   

                        return redirect('question16s')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Acceso denegado')
                #     return redirect('login')           
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question5spanish.html', context)




# ##############################################################################
# question 16


def question16Spanish(request):
    
    context = {}
    
    token_of_user = request.session['token_ses']
  
    if request.user.is_authenticated:

        # try:
        
        if 'question16s' in request.session:
            del request.session['question16s']
        else:
            pass
   
        if request.user:
                # if token_of_user:
                    # prepare question
                    question16 = QuestionsSpanish.objects.filter(id = 16).first()
                    
                    context['question'] = question16
                    context['question_tag'] = 'Pregunta 16'
                    context['question_tag_eng'] = 'Dieciséis'
                    
                    # get answers ans send form to frontend
                    
                    x_list = AnswerSpanish.objects.filter(question=question16)
                    question16Session = request.session['question16'] = []
                    
                    context['xlist'] = x_list
                    if request.method =='POST':
                        
                        list_checked = request.POST.getlist('xlist_boxes')
                        question16Session = request.session['question16s'] = []
                        
                        for i in list_checked:
                           check_answers = AnswerSpanish.objects.filter(pk=int(i))
                           question16Session.append(str(check_answers.first())) 
                           
                           
                           for ans in check_answers:
                               
                                if ans.answer == 'Tienes dificultad para concentrarte.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                    d.points +=1
                                    d.save()

                               

                                elif ans.answer == 'Te enfadas fácilmente ó estás más irritable.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                    d.points +=1
                                    d.save()

                                elif ans.answer == 'Tienes dificultad para dormir por la noche.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Te sientes ansiosa o nerviosa.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == "No puedes parar de pensar repetidamente en lo mismo.":
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                    d.points +=1
                                    d.save()
                                elif ans.answer == 'Tienes miedo a que algo malo ocurra en tu embarazo.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Anxiety')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Presentas pensamientos negativos constantemente.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Depression')
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == "Tienes sentimiento de culpa por lo problemas que presentas actualmente.":
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease ='Depression')
                                    d.points += 1
                                    d.save()
                                    
                                elif ans.answer == 'Pérdida de interés por la gente que te rodea o las actividades de la vida rutinaria.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease ='Depression')
                                  
                                    d.points +=1
                                    d.save()
                                    
                                elif ans.answer == 'Te sientes triste, baja de ánimo o con más facilidad para llorar.':
                                    d = Disease.objects.get(user_diagnosed=token_of_user, disease = 'Depression')
                                    d.points +=1
                                    d.save()
                                    
                                request.session['questions_answered_spanish'] = [1,2,3,4,5,6,7,8,9, 10, 11, 13,14,15, 16]
                                request.session.modified = True
                                
                     

                        return redirect('save_result_user')
                        # send question and answer to view
                
               
                # else:
                #     messages.warning(request, 'Acceso denegado')
                #     return redirect('login')           
        else:
                messages.warning(request, 'Usuario no verificado')
        # except:
        #     messages.warning(request, 'Error')
        #     return redirect('login')     
    else:
        messages.warning(request, 'Autenticacion requerida')
        return redirect('loginspanish')
    return render(request, 'questions/spanish/question4spanish.html', context)


# after success of test show page
@login_required(login_url="login")
def success_page_spanish(request):
    request.session.set_expiry(300)
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
    return render(request, 'pages/success_page_spanish.html', context)
