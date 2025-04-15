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

@login_required
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
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

@login_required
def logout(request):
    auth_logout(request)
    return JsonResponse({'message': 'Logout successful'})

@csrf_exempt
@require_http_methods(["POST", "GET"])
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not all([username, email, password1, password2]):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        if password1 != password2:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password1)
        return redirect('login')

    form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
