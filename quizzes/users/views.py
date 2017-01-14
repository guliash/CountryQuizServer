from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import ugettext as _

from .forms import *

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('questions:all'))
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'], form.cleaned_data['email'],
                form.cleaned_data['password'])
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('questions:all'))
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def signin(request):
    next_get = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_url = reverse('questions:all');
    if next_get:
        redirect_url = next_get
    if next_post:
        redirect_url = next_post

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_url)
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'],
                                password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(redirect_url)
            else:
                form.add_error('username', _("Can't find user"))
    else:
        form = SigninForm()
    return render(request, 'users/signin.html', {'form': form, 'next': redirect_url})

def logout_view(request):
    logout(request)
    return HttpResponse('logout')
