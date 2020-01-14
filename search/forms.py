from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label="Where are you going?", max_length=32, required=True)
