from django.urls import path
from .views import *

app_name = 'ProjectHeart'

urlpatterns = [
    path('', index, name='home-page'),
    path('passwords/', passwords, name='passwords-page'),
    path('passwords/delete/<int:id>', password_delete, name='password-delete'),
    path('passwords/update/<int:id>', password_update, name='password-update'),
]
