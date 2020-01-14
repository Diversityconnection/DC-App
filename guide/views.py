from django.shortcuts import render

from .models import GuideTour
from .forms import GuideFilterForm


def search(request):
    items = GuideTour.objects.all()

    if request.method == 'POST':
        form = GuideFilterForm(request.POST)

        if request.POST.get('country', '') != '':
            items = items.filter(country_id=request.POST['country'])
        if request.POST.get('city', '') != '':
            items = items.filter(city_id=request.POST['city'])
        if request.POST.get('price_from', '') != '':
            items = items.filter(price__gte=request.POST['price_from'])
        if request.POST.get('price_to', '') != '':
            items = items.filter(price__lte=request.POST['price_to'])
    else:
        form = GuideFilterForm()

    context = {
        'form': form,
        'items': items,
    }

    return render(request, 'list.html', context=context)


def guide_detail(request, id):
    context = {
        'item': GuideTour.objects.get(id=id)
    }
    return render(request, 'item.html', context=context)
