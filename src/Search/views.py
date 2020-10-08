from django.shortcuts import render
from ProjectHeart.models import Passwords


def search(request):
    query = request.GET.get('query')
    passwords = Passwords.objects.filter(website_name=query)

    if not passwords:
        empty = True
    elif passwords:
        empty = False

    context = {
        'passwords': passwords,
        'empty': empty,
        'query': query,
    }
    return render(request, 'extra/search.html', context)
