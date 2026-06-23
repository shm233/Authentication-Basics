from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from myapp.models import *

# Create your views here.

def signup_view(req):
    if req.method=='POST':
        username = req.POST.get('username')
        email = req.POST.get('email')
        city = req.POST.get('city')
        reg_number = req.POST.get('reg_number')
        password = req.POST.get('password')
        password2 = req.POST.get('password2')
        
        if password == password2:
            customuser.objects.create_user(
                username = username,
                email = email,
                city = city,
                reg_number = reg_number,
                password = password,
            )
            return redirect('login_view')    
    return render(req, 'signup.html')

def login_view(req):
    if req.method == 'POST':
        user_name = req.POST.get('username')
        pass_word = req.POST.get('password')
        
        user=authenticate(username=user_name, password=pass_word)
        
        if user:
            login(req,user)
            return redirect('homepage_view')
    return render(req, 'login.html')

def logout_view(req):
    logout(req)
    return redirect('login_view')

@login_required
def homepage_view(req):
    
    return render(req, 'homepage.html')
