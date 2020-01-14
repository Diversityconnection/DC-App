from django.shortcuts import render

from place.models import City
from guide.models import GuideTour
from .forms import SearchForm


def search(request):
    form = SearchForm()

    popular_guide_tours = GuideTour.objects.all()

    context = {
        'form': form,
        'popular_guide_tours': popular_guide_tours
    }

    return render(request, 'start.html', context)
