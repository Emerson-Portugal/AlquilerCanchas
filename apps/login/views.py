# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from django.middleware.csrf import get_token
import json

app_name = 'login'

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('http://127.0.0.1:8000/api/alquiler/listado/')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('http://127.0.0.1:8000/api/alquiler/listado/')

    return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect('inventario:inicioProducto')

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            form = RegisterUserForm({
                'username': data['username'],
                'password1': data['password1'],
                'password2': data['password2'],
                'email': data['email'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
            })

            if form.is_valid():
                user = form.save()
                user = authenticate(username=data['username'], password=data['password1'])
                login(request, user)
                return JsonResponse({'message': 'Registration successful!'}, status=201)
            else:
                return JsonResponse({'errors': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        form = RegisterUserForm()
        return render(request, 'registration/register.html', {'form': form})

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

def error(request):
    return render(request, 'error.html')
