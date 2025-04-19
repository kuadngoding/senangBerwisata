from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from authentication.forms import CustomUserCreationForm
import json

User = get_user_model()

@login_required(login_url='/auth/login')
def profile(request):
    user = request.user

    if request.headers.get('Content-Type') == 'application/json':
        return JsonResponse({
            'username': user.username,
            'email': user.email,
            'points': user.points,
            'registered_at': user.registered_at
        })

    context = {
        'username': user.username,
        'email': user.email,
        'points': user.points,
    }
    return render(request, 'profile.html', context)

@csrf_exempt
@require_http_methods(["POST", "GET"])
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password',
                'username': username
            })

    return render(request, 'login.html')

@login_required(login_url='/auth/login')
def logout(request):
    auth_logout(request)
    return redirect('place_list')

@csrf_exempt
@require_http_methods(["POST", "GET"])
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})
