from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User Name Is Alraedy Taken')
                return redirect('/registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email ID Is Alraedy Taken')
                return redirect('/registration')
                
            else:
                user =User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                messages.info(request,'User Created')
                subject = "Registration on Auction Web"
                from_email = settings.EMAIL_HOST_USER
                to_email = [email]
                
                signup_message = "Thanks for registering with Auction Web. Start your auction today with Auction Web"
                send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False)
                return redirect('login')
        else:
            messages.info(request,'Password Not Match')
            return render(request,'auctions/register.html')

    else:
        return render(request,'auctions/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
            
        else:
            messages.info(request,'Invalid Credentials')
            return render(request,'auctions/login.html')


    else:
        return render(request,'auctions/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')