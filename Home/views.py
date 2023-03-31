from django.shortcuts import render
from .models import Product

# Create your views here.

def home_view(request):
    product = Product.objects.all()[:5]
    email = None

    if request.user.is_authenticated:
       email = request.user.email
 
    context = {'products':product,
              'email': email}
    return render(request,"index.html",context = context)

def about_view(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email
 
    context = {
               'email': email
               }
    return render(request,"about.html",context = context)

def shop_view(request):
    product = Product.objects.all()
    email = None
    if request.user.is_authenticated:
        email = request.user.email
 
    context = {'products':product,
               'email': email}
    return render(request,"shop-left-sidebar.html",context=context)

def contact_view(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email
 
    context = {
               'email': email
               }
    return render(request,"contact.html",context=context)

def my_account_view(request):
    if request.user.is_authenticated:
        email = request.user.email
        first_name = request.user.first_name
        
 
    context = {
               'email': email,
               'first_name':first_name
               }
    return render(request,"my-account.html",context=context)

def product_view(request):
    product = Product.objects.all()
    email = None
    if request.user.is_authenticated:
        email = request.user.email
 
    context = {'products':product,
               'email': email}
    return render(request,"single-product.html",context=context)
