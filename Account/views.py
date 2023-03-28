from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from Home.forms import CreateUserForm,EditProfileForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,"Successfully Login")
            return redirect('/')
        else:
            messages.success(request,"Invalid Credentials")
            return redirect("/login")
    else:
        form = AuthenticationForm()
        
    return render(request, 'login-register.html', {'form': form, 'form_type': 'login'})

def logout_view(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect("/login")

def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = CreateUserForm()
    return render(request, 'login-register.html', {'form': form, 'form_type': 'register'})

def edit_profile_view(request):

    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
            return redirect("/my-account")
    else:
        form = EditProfileForm(instance = request.user)
    
    return render(request, 'my-account.html', {'form': form, 'form_type': 'edit'})

