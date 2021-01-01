from django.contrib import admin
from .models import Passwords


class PasswordsAdmin(admin.ModelAdmin):
    list_display = ['website_name', 'website_url',
                    'username', 'email', 'password']
    fields = ['website_name', 'website_url', 'username', 'email', 'password']
    list_filter = ['username', 'email', 'website_name']


admin.site.register(Passwords, PasswordsAdmin)
