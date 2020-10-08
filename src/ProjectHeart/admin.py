from django.contrib import admin
from .models import Passwords


class PasswordsAdmin(admin.ModelAdmin):
    list_display = ['website_name', 'website_url', 'password_hashed']
    fields = ['website_name', 'website_url', 'password']
    list_filter = ['website_name']


admin.site.register(Passwords, PasswordsAdmin)
