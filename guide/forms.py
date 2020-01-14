from django import forms

from place.models import Country, City


class GuideFilterForm(forms.Form):
    price_from = forms.DecimalField(required=False)
    price_to = forms.DecimalField(required=False)
    country = forms.ModelChoiceField(Country.objects.all(), required=False)
    city = forms.ModelChoiceField(City.objects.all(), required=False)
