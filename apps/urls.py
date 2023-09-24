from django.urls import path
from .views import *
from .spanish_views import *


# 
urlpatterns = [
    # admin functions 
    path('manage_access', manage_user, name='manage_access'),
    path('admin_result', dashboard_result_view, name='admin_result'),
    path('details/<int:pk>', details, name='details'),
    path('home', Homepage, name='home'),
    path('homes', HomepageSpanish, name='homes'),
    # path('pdf', Generate_pdf.as_view()),
    path('success_page', success_page, name='success_page'),
    path('success_page_spanish', success_page_spanish, name='success_page_spanish'),
    path('save_result_user', save_result_user, name='save_result_user'),
    path('contact', contact, name='contact'),
    path('contactspanish', contactspanish, name='contacts'),
    
    # questions 
    path('question1', question1, name='question1'),
    path('question2', question2, name='question2'),
    path('question3', question3, name='question3'),
    path('question4', question4, name='question4'),
    path('question5', question5, name='question5'),
    path('question6', question6, name='question6'),
    path('question7', question7, name='question7'),
    path('question8', question8, name='question8'),
    path('question9', question9, name='question9'),
    path('question10', question10, name='question10'),
    path('questionCs', questionCombined, name='questionCs'),
    # path('question15', question15, name='question15'),
    # path('question16', question16, name='question16'),
    
    # questions in spanish
    
    path('question1S', question1Spanish, name='question1s'),
    path('question2S', question2Spanish, name='question2s'),
    path('question3S', question3Spanish, name='question3s'),
    path('question4S', question4Spanish, name='question4s'),
    path('question5S', question5Spanish, name='question5s'),
    path('question6S', question6Spanish, name='question6s'),
    path('question7S', question7Spanish, name='question7s'),
    path('question8S', question8Spanish, name='question8s'),
    path('question9S', question9Spanish, name='question9s'),
    path('question10S', question10Spanish, name='question10s'),
    path('questionCsS', questionCombinedSpanish, name='questionCss'),
    # path('question15S', question15Spanish, name='question15s'),
    # path('question16S', question16Spanish, name='question16s'),
    
    # choose language
    path('', choose_language, name='language'),
    
    # result
    path('results', ViewPDFSpanish.as_view(), name='vresults'),
    path('result', ViewPDF.as_view(), name='vresult'),
    path('downloads', DownloadPDFSpanish.as_view(), name='dresults'),
    path('download', DownloadPDF.as_view(), name='dresult'),
    
]
    
    

