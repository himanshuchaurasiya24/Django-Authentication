from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin 

class CustomUserAdmin(UserAdmin):
    list_display= ('username', 'email', 'first_name', 'last_name', 'facebook', 'twitter', 'instagram')

admin.site.register(CustomUser, CustomUserAdmin)

