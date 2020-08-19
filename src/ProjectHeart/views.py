from django.shortcuts import render
from .forms import PasswordsForm
from .models import Passwords

def index(request):
    # user = Passwords.objects.get(user=request.user)
    form = PasswordsForm(request.POST or None)
    context = {
        "form": form
    }
    return render(request, "home/home.html", context)

def profile(request):
    context = {

    }
    return render(request, "personal/profile.html", context)
