from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Online Car Rental system Admin"
admin.site.site_title = "Online Car Rental system Admin Portal"
admin.site.index_title = "Welcome to Online Car Rental system"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('contact.urls')),
    path('', include('registers.urls')),
    path('', include('login.urls')),
    # path('', include('booking_details.urls')),
    path('', include('carlist.urls')),
    # path('', include('about.urls')),
    # path('', include('authenticate.urls')),
]