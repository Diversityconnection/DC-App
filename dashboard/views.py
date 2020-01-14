from django.shortcuts import render

from guide.models import GuideTour
from .forms import GuideForm


def dashboard(request):
    guide_tours = GuideTour.objects.filter(owner__user=request.user)

    context = {
        'guide_tours': guide_tours,
    }

    return render(request, 'dashboard.html', context=context)


def guide(request):
    form = GuideForm()

    context = {
        'form': form
    }

    return render(request, 'guide.html', context)
