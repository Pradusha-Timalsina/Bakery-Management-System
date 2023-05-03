from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.


def home(request):
    email = None
    products = Product.objects.all()
    if request.user.is_authenticated:
        email = request.user.email
        print(request.user)
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']
    
    context = {
        'order':order,
        'email':email,
        'products':products,
        'cartItems':cartItems,
    }
    

    return render(request,'index.html',context=context)


def about(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
        'get_cart_total':0,
        'get_cart_items':0,
        'shipping': False,
        }
        cartItems = order['get_cart_items']
    
    context = {
        'order':order,
        'email':email,
        'cartItems':cartItems,
    }

    return render(request,'about.html',context=context)


def shop(request):
    email = None
    products = Product.objects.all()
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']
    
    context = {
        'order':order,
        'email':email,
        'products':products,
        'cartItems':cartItems,
    }
    return render(request,'shop-left-sidebar.html',context=context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    email = None
    if request.user.is_authenticated:
        email = request.user.email
 
    context = {'product':product,
               'email': email}
    return render(request,"single-product.html",context=context)

def contact(request):
    email=None
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']
    
    context = {
        'order':order,
        'email':email,
        'cartItems':cartItems,
    }
    return render(request,'contact.html',context=context)

def account(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']
    
    context = {
        'order':order,
        'email':email,
     
        'cartItems':cartItems,
    }
    return render(request,'my-account.html',context=context)


def cart(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
       
    else:
        items = []
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']
    
    context = {
        'order':order,
        'email':email,
        'items':items,
        'cartItems':cartItems,
    }
    return render(request,'cart.html',context=context)


def billing_details(request):

    if request.method == 'POST':
        # Process form data here
        return redirect('ordersummary')
    
    return render(request,"billing.html",context={})


def orderSummary(request):

    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer,complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        print(items)
    else:
        items = []
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']
    
    context = {
        'order':order,
        'email':email,
        'items':items,
        'cartItems':cartItems,
    }
    
    return render(request,'orderSummary.html',context=context)



def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('Product:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,Product=product)
    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('Item was added',safe=False)

