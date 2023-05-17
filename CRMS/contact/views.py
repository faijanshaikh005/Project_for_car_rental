from django.shortcuts import render, HttpResponse
from datetime import datetime
from contact.models import Contact 
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def about(request):
    return render(request, 'about.html') 

def customerdashboard(request):
    return render(request, 'customer_dashboard.html')

# def services(request):
#     return render(request, 'services.html') 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


# def Book_car(request):
#     return render(request, 'BookYourCar.html')

def Cars(request):
    return render(request, 'Cars.html') 

# # def index(request):
# #     return render(request, 'contact us.html') 

# def login(request):
#     return render(request, 'login.html') 

def recover_forgot_password(request):
    return render(request, 'recover forgot password.html') 

def Register(request):
    return render(request, 'register.html') 