from django.shortcuts import render
from .forms import PasswordsForm
from django.contrib.auth.decorators import login_required
from .models import Passwords
from django.http import HttpResponseRedirect


# Homepage view
def index(request):
    form = PasswordsForm(request.POST or None)
    created = False

    if request.method == "POST":
        if request.user.is_authenticated:
            if form.is_valid:
                form.save()
                created = True

    context = {
        "form": form,
        "created": created
    }
    return render(request, "home/home.html", context)


# Password list
@login_required
def passwords(request):
    passwords = Passwords.objects.all().order_by('website_name')

    if not passwords:
        empty = True
    elif passwords:
        empty = False
    context = {
        'passwords': passwords,
        'empty': empty
    }
    return render(request, "passwords/passwords.html", context)


# Password delete
@login_required
def password_delete(request, id):
    password = Passwords.objects.get(id=id)
    password.delete()

    return HttpResponseRedirect('/passwords/')


# Password update
@login_required
def password_update(request, id):
    password = Passwords.objects.get(id=id)
    form = PasswordsForm(request.POST or None, instance=password)

    if request.method == "POST":
        if request.user.is_authenticated:
            if form.is_valid:
                form.save()
                return HttpResponseRedirect('/passwords/')

    context = {
        'id': id,
        'form': form,
    }
    return render(request, 'passwords/update.html', context)
