# from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.models import User
# # from django.contrib.auth import logout, authenticate, login
# from datetime import datetime
# # from booking_details.models import Car_Booking_details
# from django.contrib import messages

# # Create your views here.



# def BookYourCar(request):
#     # if request.method == "POST":
#     #     Pick_up_date = request.POST.get('pickup')
#     #     car_name = request.POST.get('carname')
#     #     car_company_name = request.POST.get('carcompany')
#     #     car_rent_per_day = request.POST.get('carrent')
#     #     Car_type = request.POST.get('cartype')
#     #     BookYourCar = Car_Booking_details(Pick_up_date=pickup, car_name=carname, car_company_name=carcompany, desccar_rent_per_day=carrent, Car_type=cartype)
#     #     BookYourCar.save()
#     #     messages.success(request, 'Your car booking successfull!')
#     # print(request.POST)
#     return render(request, 'BookYourCar.html')


# def registers(request):
#     return render(request, 'login.html') 
    

# def customerdashboard(request):
#     return render(request, 'customer_dashboard.html')

# def tata(request):
#     return render(request, 'tata.html')

# def index(request):
#     return render(request, 'index.html')


# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

# def Cars(request):
#         return render(request, 'Cars.html')

# def loginUser(request):
#         return render(request, '/login')

   


# def recover_forgot_password(request):
#     return render(request, 'recover forgot password.html')




# def logoutUser(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("/login")