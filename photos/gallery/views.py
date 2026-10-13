from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def home(request):
    return render(request, 'gallery/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'gallery/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('gallery_home')

        return render(
            request,
            'gallery/login.html',
            {'error': 'Invalid username or password.'},
        )

    return render(request, 'gallery/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')


@login_required
def gallery_home(request):
    return render(request, 'gallery/gallery_home.html')
