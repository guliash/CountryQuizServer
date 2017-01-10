from django.shortcuts import render
from django.http import HttpResponse

def signup(request):
    return HttpResponse('signup')

def signin(request):
    return HttpResponse('signin')

def logout(request):
    return HttpResponse('logout')
