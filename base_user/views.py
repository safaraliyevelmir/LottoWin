from django.conf import settings
from django.http import request
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages
import uuid
from django.core.mail import send_mail
from django.contrib.auth import get_user_model, login,logout,authenticate
from base_user.utils import captcha
from django.contrib.auth.views import  PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

User = get_user_model()

def register(request):
    cap = captcha()
    form = UserRegisterForm()
    if request.method == 'POST':
        captcha_secret = request.POST.get('captcha_secret')
        captcha_input = request.POST.get('captcha')
        if captcha_secret == captcha_input:
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                if obj.privacy_policy == False:
                    messages.error(request,'You must accept privacy policy')
                    return redirect('register')
                else:
                    obj.token = str(uuid.uuid4())
                    obj.is_active = False
                    obj.save()
                    token = obj.token
                    email = obj.email
                    send_email(token,email)
                    return redirect('login')
        else:
            messages.error(request,"Captcha is not correct")
    context = {
        'form':form,
        'cap':cap
    }
    return render(request,'register.html',context)

def send_email(token,email):
    subject = 'Your verified Email'
    message = f"you can verifed your account is http://127.0.0.1:8000/accounts/success/{token} here"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,from_email,recipient_list)

def success(request,token):
    obj = User.objects.filter(token=token).first()
    obj.is_active = True
    obj.save()
    return redirect('login')

def loginUser(request):
    cap = captcha()
    if request.method == 'POST':
        captcha_secret = request.POST.get('captcha_secret')
        captcha_input = request.POST.get('captcha')
        if captcha_secret == captcha_input:

            email = request.POST.get('email')
            password = request.POST.get('password')
            user_obj = User.objects.filter(email=email).first()
            if user_obj is None:
                messages.error(request,"User not found")
                return redirect('login')
        
            user = authenticate(email=email,password=password)

            if user is not None:
                login(request,user)
                return redirect('core:index')
            else:
                messages.error(request,"Password is incorrect")
                return redirect('login')
        else:
            messages.error(request,"captcha is not correct")
            return redirect('login')   
    context = {
        'cap':cap
    }

    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')