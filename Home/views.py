from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .models import Product,Customer

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


from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from .forms import MySetPasswordForm
from django.contrib import messages

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = MySetPasswordForm
    success_url = reverse_lazy('password_reset_complete') # This is the URL to redirect to
    template_name = 'reset.html'
    redirect_field_name = 'reset_password_complete'  # specify the name of the GET parameter

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your password has been reset.")
        return response