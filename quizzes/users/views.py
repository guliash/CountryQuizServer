from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import *

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['name'], form.cleaned_data['email'],
                form.cleaned_data['password'])
            user.save()
            return HttpResponseRedirect(reverse('questions:all'))
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def signin(request):
    return HttpResponse('signin')

def logout(request):
    return HttpResponse('logout')
