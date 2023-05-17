from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from django.contrib import messages
# Create your views here.


# def index(request):
#     print(request.user)
#     if request.user.is_anonymous:
#         return redirect("/admin_login") 
#     return render(request, 'admin_homepage.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

    else:
         return render(request, 'admin_homepage.html')

def logoutUser(request):
    logout(request)
    return redirect("/admin_login")


def homepage(request):
    return redirect("/admin_homepage")