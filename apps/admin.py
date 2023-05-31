from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Questions)
admin.site.register(QuestionsSpanish)
admin.site.register(Answer)
admin.site.register(AnswerSpanish)
admin.site.register(Disease)

admin.site.register(Mom_data)
admin.site.register(Disease_result)
admin.site.register(Result_owner)
