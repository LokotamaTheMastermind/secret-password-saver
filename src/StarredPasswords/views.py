from django.shortcuts import render


def homepage(request):
    context = {}
    return render(request, 'starred/page.html', context)
