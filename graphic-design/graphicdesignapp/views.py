from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from graphicdesignapp.models import User
import re

# Create your views here.

# TODO : check this view
# def index(request):
#     return HttpResponse(content="index")


def check(email):
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(email_regex, email)):
        return True
    else:
        return False


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if len(name) >= 5 and check(email) and len(password) >= 8:
            user = User.objects.all().filter(email=email)
            # Check if email exist
            if user:
                messages.error(request, "User with Email Exist")
                return redirect('register')
            user = User()
            user.name = name
            user.password = make_password(password)
            user.email = email
            user.save()
            # messages.success(request, "User Registered Successfully")
            return redirect('login')
        else:
            if len(name) < 5:
                messages.error(
                    request, "Name should be atleast 5 characters long and not empty", )
            if not check(email):
                messages.error(request, "Email must be an email")
            if len(password) < 8:
                messages.error(
                    request, "Password must be 8 characters long")
    return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if check(email) and len(password) >= 8:
            user = User.objects.all().filter(email=email).first()
            if user:
                if check_password(password, user.password):
                    return redirect('dashboard')
                else:
                    messages.error(request, "Incorrect Password")
                    return redirect('login')
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('login')
        else:
            if not check(email):
                messages.error(request, "Email must be an email")
            if len(password) == 0:
                messages.error(request, "Password Cannot Be Empty")
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def logout(request):
    return HttpResponse(content="logout")
