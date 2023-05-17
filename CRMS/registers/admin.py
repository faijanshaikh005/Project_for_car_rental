from django.contrib import admin
from .models import signup
# Register your models here.

@admin.register(signup)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
signup._meta.get_fields()]