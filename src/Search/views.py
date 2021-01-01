from django.db.models.query_utils import Q
from django.shortcuts import render
from ProjectHeart.models import Passwords


def search(request):
    query = request.GET.get('query')

    if query is not None:
        lookups = Q(website_name__icontains=query) | Q(
            username__icontains=query) | Q(email__icontains=query)

        result = Passwords.objects.filter(lookups).distinct()
        empty = False
    else:
        empty = True
        result = None

    context = {
        'empty': empty,
        'query': query,
        'results': result
    }
    return render(request, 'extra/search.html', context)
