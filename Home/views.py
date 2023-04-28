from django.shortcuts import get_object_or_404, render
from .models import Customer, Product,Order
from django.contrib.auth.decorators import login_required

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

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    email = None
    if request.user.is_authenticated:
        email = request.user.email
 
    context = {'product':product,
               'email': email}
    return render(request,"single-product.html",context=context)

@login_required
def cart(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

        for item in items:
            print(item.Product)
      
    else:
        items = []
    context = {'items': items, 'email': email}
    return render(request, "cart.html", context=context)

