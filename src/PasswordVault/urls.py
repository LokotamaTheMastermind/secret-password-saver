""" Project Routes """

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ProjectHeart.urls")),
    path('search/', include('Search.urls')),
    path('starred/', include('StarredPasswords.urls'))
]
