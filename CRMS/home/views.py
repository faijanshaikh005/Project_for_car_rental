from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
# from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from carlist.models import cars
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def forgot(request):
    return render(request, 'recover forgot password.html') 

def car(request):
    m1 = cars.objects.all()
    return render(request,'cardetails.html',{'m':m1})


def tata(request):
    return render(request, 'tata.html') 

def toyota(request):
    return render(request, 'toyota.html') 

def mahindra(request):
    return render(request, 'mahindra.html') 

def mg(request):
    return render(request, 'mg.html') 

def kia(request):
    return render(request, 'kia.html') 

def volkswagen(request):
    return render(request, 'volkswagen.html') 

def force(request):
    return render(request, 'force.html') 

def maruti(request):
    return render(request, 'maruti.html') 

def honda(request):
    return render(request, 'honda.html') 

def hyundai(request):
    return render(request, 'hyundai.html') 


def about(request):
    return render(request, 'about.html') 

# def services(request):
#     return render(request, 'services.html') 

def contact(request):
     return render(request, 'contact.html')


def Cardetails(request):
    return render(request, 'BookYourCar.html')
    # return redirect("BookYourCar.html") 
    #  return render(request, 'BookYourCar.html')

def Cars(request):
    return render(request, 'Cars.html') 

# # def index(request):
# #     return render(request, 'contact us.html') 

def recover_forgot_password(request):
    return render(request, 'recover forgot password.html') 

# def recover_forgot_password(request):
#     return render(request, 'recover forgot password.html') 

def Register(request):   
    return render(request, 'register.html')

def customerdashboard(request):
    return render(request, 'customer_dashboard.html')

# --------------------------------------------------------



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

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")