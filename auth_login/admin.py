from django.contrib import admin

from auth_login.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']

