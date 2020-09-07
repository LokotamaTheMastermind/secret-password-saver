from django.shortcuts import render
from .forms import PasswordsForm
from .models import Passwords
from django.contrib.auth.decorators import login_required

def index(request):
    # user = Passwords.objects.get(user=request.user)
    form = PasswordsForm(request.POST or None)
    
    context = {
        "form": form
    }
    return render(request, "home/home.html", context)

@login_required
def profile(request):
    context = {

    }
    return render(request, "personal/profile.html", context)
