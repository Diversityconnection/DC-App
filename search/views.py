from django.shortcuts import render

from place.models import City
from .forms import SearchForm


def search(request):
    form = SearchForm()

    popular_destinations = City.objects.all()

    context = {
        'form': form,
        'popular_destinations': popular_destinations,
    }

    return render(request, 'start.html', context)
