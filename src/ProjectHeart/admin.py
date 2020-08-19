from django.contrib import admin
from .models import Passwords

class PasswordsAdmin(admin.ModelAdmin):
    list_display = ['user', 'website_name', 'website_url', 'password_hashed']
    fields = ['user', 'website_name', 'website_url', 'password']
    list_filter = ['user', 'website_url']

admin.site.register(Passwords, PasswordsAdmin)
