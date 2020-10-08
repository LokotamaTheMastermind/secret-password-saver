from django.urls import path
from .views import *

app_name = 'Search'

urlpatterns = [
    path('', search, name='search-query')
]
