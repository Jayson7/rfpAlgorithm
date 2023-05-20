from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(Disease)

admin.site.register(Mom_data)
