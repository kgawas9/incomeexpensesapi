from django.contrib import admin

from .models import User
# Register your models here.

@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email','username','password','is_active','is_superuser','is_verified'
    ]
