from django import forms

from guide.models import GuideTour


class GuideForm(forms.ModelForm):
    class Meta:
        model = GuideTour
        fields = ['title', 'description', 'duration', 'price', 'country', 'city']
