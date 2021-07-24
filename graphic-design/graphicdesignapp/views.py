from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls.conf import path
from graphicdesignapp.models import Design
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http.response import JsonResponse
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
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        if len(username) >= 5 and check(email) and len(password) >= 8 and len(firstname) >= 5 and len(lastname) >= 5:
            isUserPresent = User.objects.all().filter(username=username).exists()
            # Check if email exist
            if isUserPresent:
                messages.error(request, "User with username Exist")
                return redirect('register')
            createdUser = User.objects.create(
                username=username, email=email, password=make_password(password))
            createdUser.first_name = firstname
            createdUser.last_name = lastname
            createdUser.save()
            # messages.success(request, "User Registered Successfully")
            return redirect('login')
        else:
            if len(username) < 5:
                messages.error(
                    request, "UserName should be atleast 5 characters long and not empty")
            if len(firstname) < 5:
                messages.error(
                    request, "Firstname should be atleast 5 characters long and not empty")
            if len(lastname) < 5:
                messages.error(
                    request, "Lastname should be atleast 5 characters long and not empty")
            if not check(email):
                messages.error(request, "Email must be an email")
            if len(password) < 8:
                messages.error(
                    request, "Password must be 8 characters long")
    return render(request, 'register.html')


def handleLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if len(username) > 0 and len(password) >= 8:
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successfull")
                return redirect('dashboard')
            else:
                messages.error(
                    request, "Invalid Credentials, Please Try again...")
        else:
            if len(username) == 0:
                messages.error(request, "Username cannot be empty")
            if len(password) == 0:
                messages.error(request, "Password Cannot Be Empty")
    return render(request, 'login.html')


def getdesigns(request):
    designs = Design.objects.all()
    serialized_data = serializers.serialize('python', designs)
    return JsonResponse(serialized_data, safe=False)


@login_required(login_url='/accounts/login')
def getdesignsbyid(request, design_id):
    design = Design.objects.get(id=design_id)
    return render(request, 'single_design.html', {
        'design': design
    })


def dashboard(request):
    return render(request, 'dashboard.html')


def handleLogout(request):
    logout(request)
    messages.success(request, "Logout success")
    return redirect('dashboard')
