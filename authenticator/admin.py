from django.contrib import admin
from .models import * 

# Register your models here.

admin.site.register(GeneratedPassword)
admin.site.register(RegisterClient)
admin.site.register(Password_log_on_user)
admin.site.register(PasswordStorage)
admin.site.register(Usage_Monitor)

admin.site.register(UserLoginToken)
