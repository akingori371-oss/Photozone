from django.shortcuts import render


def home(request):
    return render(request, "gallery/home.html")


def login(request):
    return render(request, "gallery/login.html")
