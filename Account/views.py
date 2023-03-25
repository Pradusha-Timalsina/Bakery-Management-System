from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from Home.forms import CreateUserForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login-register.html', {'form': form, 'form_type': 'login'})

def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = CreateUserForm()
    return render(request, 'login-register.html', {'form': form, 'form_type': 'register'})
