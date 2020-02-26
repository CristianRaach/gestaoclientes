from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')


def center(request):
    return render(request, 'center.html')


def works(request):
    return render(request, 'works.html')