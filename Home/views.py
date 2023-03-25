from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse



from .forms import CreateUserForm
from .models import Customer,Product

# Create your views here.


def home_view(request):
    product = Product.objects.all()[:5]
    email = None
    if request.user.is_authenticated:
        email = request.user.email
 
    context = {'products':product,
               'email': email}
    return render(request,"index.html",context=context)

def about_view(request):
    return render(request,"about.html")

def shop_view(request):
    return render(request,"shop-left-sidebar.html")

def contact_view(request):
    return render(request,"contact.html")

def my_account_view(request):
    return render(request,"my-account.html")



