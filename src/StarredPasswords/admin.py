from django.contrib import admin
from .models import StarredPasswords


class StarredPasswordAdmin(admin.ModelAdmin):
    list_display = ['password']


admin.site.register(StarredPasswords, StarredPasswordAdmin)
