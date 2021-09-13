from django.contrib import admin
from .models import User





class UserAdmin(admin.ModelAdmin):
    fields = ['username','email','first_name','last_name','country','phone_number','is_superuser','is_staff','is_active']
    list_display = ['email','full_phone_number','is_active']



admin.site.register(User,UserAdmin)