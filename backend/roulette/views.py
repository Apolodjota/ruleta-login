from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        User.objects.create_user(username=request.POST['email'], password=request.POST['password'])
        return redirect('login')
    return render(request, 'roulette/register.html')


# backend/roulette/views.py
def login_view(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('roulette')
    return render(request, 'roulette/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def roulette_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'roulette/roulette.html')

