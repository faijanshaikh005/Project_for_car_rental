from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from datetime import datetime
from registers.models import signup
from django.contrib import messages



def registers(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        dateofbirth = request.POST.get('dateofbirth')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
       
    # if len(phone) != 10:
    #     messages.error(request, 'Number should be 10 digit')
    #     return render(request, 'register.html')
        
    # elif password != cpassword:
    #     messages.error(request, 'Password and confirm password did not match')
    #     return render(request, 'register.html')
        
    # else:
        # registers = signup(name=name, gender=gender, email=email, phone=phone, dateofbirth=dateofbirth(), cpassword=cpassword, password=password)
        # registers.save()
        # messages.success(request, 'Your account successfully created')
        # print(request.POST)
    return render(request, 'login.html') 
        
        # save(request.POST)
        # messages.success(request, message)(request, 'Your account successfully created')
        # return render(request, 'login.html') 
 

def customerdashboard(request):
    return render(request, 'customer_dashboard.html')

def tata(request):
    return render(request, 'tata.html')

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


# def Book_your_car(request):
   
#     return render(request, 'BookYourCar.html')


def Cars(request):
        return render(request, 'Cars.html')

def loginUser(request):
    if request.method=="POST":
        name = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(name=username, password=password)
        return render(request, 'index.html')
        

    else:
            # No backend authenticated the credentials
        return render(request, '/login')

   


def recover_forgot_password(request):
    return render(request, 'recover forgot password.html')




def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/login")