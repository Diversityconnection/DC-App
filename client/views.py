from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from cuser import forms

from .models import Client, ClientRole


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))

    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponseRedirect(reverse('login'))
    else:
        form = forms.AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def registration(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('dashboard'))

    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(user=user, role=ClientRole.CUSTOMER)
            auth.login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = forms.UserCreationForm()

    return render(request, 'registration.html', {'form': form})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('login'))
