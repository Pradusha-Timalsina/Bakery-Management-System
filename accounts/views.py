from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from Home.models import Customer

from .forms import CustomerForm
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        # Get login form data
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        # Get registration form data
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # Create new User object
        user = User.objects.create_user(username, email, password)
        # Create new Customer object and associate it with User object
        customer = Customer.objects.create(user=user, name=name, username=username, email=email, password=password)
        # Log in user and redirect to index page
        login(request, user)
        return redirect('login')
    else:
        # Render registration page
        return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('login')
