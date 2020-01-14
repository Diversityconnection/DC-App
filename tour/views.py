from django.shortcuts import render


def search(request):
    items = []
    return render(request, 'results.html', {'items': items})
