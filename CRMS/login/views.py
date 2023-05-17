from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, login


def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        
        user = authenticate(username=username, password=password)

        if user is not None:
           
            login(request, user)
            return redirect("/")

        else:
            return render(request, '/login')

    return render(request, '/login')


def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login")

# ---------------------------------------------------------------------------------------------

def adminUser(request):
    # if request.user.is_anonymous:
    #     return redirect("/admin_login") 
 return render(request, 'admin_login.html')

def homepage(request):
    return render(request,'admin_homepage.html')


def adminLogin(request):
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
            # No backend authenticated the credentials
            return render(request, 'admin_homepage.html')  

    return render(request, 'admin_homepage.html')