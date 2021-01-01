from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import PasswordsForm
from django.contrib.auth.decorators import login_required
from .models import Passwords
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


# Homepage view
def index(request):
    form = PasswordsForm(request.POST or None)
    created = False

    if request.method == "POST":
        if request.user.is_authenticated:
            if form.is_valid:
                form.save()
                form = PasswordsForm()
                created = True

    context = {
        "form": form,
        "created": created
    }
    return render(request, "home/home.html", context)


# Logout view
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


# Password list
@login_required
def passwords(request):
    passwords = Passwords.objects.all().order_by('website_name')
    page = request.GET.get('page', 1)

    paginator = Paginator(passwords, 5)
    number_of_results = paginator.count

    try:
        passwords = paginator.page(page)
    except PageNotAnInteger:
        passwords = paginator.page(1)
    except EmptyPage:
        passwords = paginator.page(paginator.num_pages)

    if not passwords:
        empty = True
    elif passwords:
        empty = False

    context = {
        'passwords': passwords,
        'empty': empty,
        'num_of_results': number_of_results,
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
