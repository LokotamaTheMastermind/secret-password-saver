from django.urls import path
from .views import index, profile

urlpatterns = [
    path('', index, name='home-page'),
    path('profile/', profile, name='profile-page'),
]
