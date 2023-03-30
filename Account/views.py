from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Home.forms import CreateUserForm


from django.contrib import messages


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
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('/login')
        else:
            messages.error(request, 'There was an error registering. Please try again.')
    else:
        form = CreateUserForm()
    return render(request, 'login-register.html', {'form': form, 'form_type': 'register'})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.phone_number = request.POST.get('phone_number',user.phone_number)
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if password and user.check_password(password):
            if new_password and new_password == confirm_password:
                user.set_password(new_password)
                messages.success(request, 'Password changed successfully')
            user.save()
            messages.success(request, 'Profile updated successfully')
        elif password or new_password or confirm_password:
            messages.error(request, 'Invalid password')
        else:
            user.save()
            messages.success(request, 'Profile updated successfully')
    return redirect('my-account')



