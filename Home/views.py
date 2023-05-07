from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from django.http import HttpResponse, JsonResponse
import json
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import requests
from reportlab.pdfgen import canvas
import random
# Create your views here.


def home(request):
    email = None
    products = Product.objects.all()
    order = None
    
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_total': 0,
            'get_cart_items': 0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']
    
    context = {
        'order': order,
        'email': email,
        'products': products,
        'cartItems': cartItems,
    }

    return render(request, 'index.html', context=context)



def about(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
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
    category = Category.objects.all()
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
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
        'category':category,
    }
    return render(request,'shop-left-sidebar.html',context=context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    email = None
    
    if request.method == 'POST':
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')
        user = request.user
        review = Review(product=product, user=user, rating=rating, comment=comment)
        review.save()
        
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
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
        'product':product,
        'related_products':related_products,
        'cartItems':cartItems,
    }
    return render(request, 'single-product.html', context=context)


def product_list(request, category):
    products = Product.objects.filter(category__name=category)
    context = {'products': products, 'category': category}
    return render(request, 'shop2.html', context)


def contact(request):
    email=None
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
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
    name = None
    orders = None  # new variable to store orders
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        name = customer.name
        phone = customer.phone
        
        orders = Order.objects.filter(customer=customer).order_by('-date_orderd')  # get all orders of the customer and order them by date_orderd
        order = Order.objects.filter(customer=customer, complete=False).first()
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        cartTotal = order.get_cart_total
    else:
        items = []
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping': False,
        }
        cartItems = order['get_cart_items']
        cartTotal = order['get_cart_total']

    context = {
        'order':order,
        'email':email,
        'name':name,
        'cartItems':cartItems,
        'cartTotal':cartTotal,  # add the total cart price to the context
        'orders': orders,  # pass the orders to the context
    }
    print(cartItems)
    print(cartTotal)
    return render(request,'my-account.html',context=context)



def cart(request):
    email = None
    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
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


def billingDetails(request):
    if request.method == 'POST':
        # Store the form data in a session variable or cache
        request.session['shipping_details'] = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'address': request.POST['address'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'zip': request.POST['zip'],
        }
        return redirect('payment') # Redirect to payment page after successful submission
    
    return render(request, 'billing.html')


def orderSummary(request):

    if request.user.is_authenticated:
        email = request.user.email
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
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
    order = Order.objects.filter(customer=customer, complete=False).first()
    orderItem, created = OrderItem.objects.get_or_create(order=order,Product=product)
    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('Item was added',safe=False)


def payment(request):
    # Retrieve the stored shipping details from the session variable or cache
    shipping_details = request.session.get('shipping_details', {})
    if not shipping_details:
        # Handle case where shipping details have not been submitted yet
        return redirect('billing')

    if request.method == 'POST':
        # Process payment and create a new ShippingAddress instance to save to the database
        customer = request.user.customer
        order = Order.objects.create(customer=customer, complete=True)
        shipping_address = ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=shipping_details['address'],
            city=shipping_details['city'],
            state=shipping_details['state'],
            zipcode=shipping_details['zip'],
        )

        # transaction_id = random.randint(100000, 999999)

        # # Assign the transaction id to the order instance
        # order.transaction_id = transaction_id

        # Add success message to session
        messages.success(request, 'Payment successful!')

        return redirect('payment_success') # Redirect to success page after successful payment
    else:
        print(shipping_details)
        return render(request, 'payment.html')


def payment_success(request):
    customer = request.user.customer
    order = Order.objects.create(customer=customer, complete=True)
    transaction_id = order.transaction_id
    amount = order.get_cart_total

    print(transaction_id)
    print(amount)
    context = {
        'transaction_id':transaction_id,
        'amount':amount,
    }
    return render(request, 'payment_success.html',context=context)

def khalti_payment(request):
    shipping_details = request.session.get('shipping_details', {})
    # Retrieve the order and shipping address details
    customer = request.user.customer
    order = Order.objects.create(customer=customer, complete=True)
    shipping_address = ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=shipping_details['address'],
            city=shipping_details['city'],
            state=shipping_details['state'],
            zipcode=shipping_details['zip'],
        )
    shipping_address = ShippingAddress.objects.get(order=order)
    
    # Calculate the total amount to be paid
    total = order.get_cart_total

    if request.method == 'POST':
        # Retrieve the token and amount from the Khalti payment form
        token = request.POST.get('token')
        amount = request.POST.get('amount')
        
        # Make a request to the Khalti API to verify the payment
        url = 'https://khalti.com/api/v2/payment/verify/'
        payload = {
            'token': token,
            'amount': amount
        }
        headers = {
            'Authorization': 'test_secret_key_78ad81d208c442e2b3c18e4ac179289a'
        }
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        
        # Check if the payment was successful
        if data['idx']:
            # Update the order and shipping address details
            order.transaction_id = data['idx']
            order.complete = True
            order.save()
            shipping_address.save()
            print(order.transaction_id)
            print("hello")
            
            # Add success message to session
            messages.success(request, 'Payment successful!')

            return redirect('payment_success') # Redirect to success page after successful payment
        else:
            # Add error message to session
            messages.error(request, 'Payment failed. Please try again.')

    # Render the Khalti payment page with the total cost and shipping address details
    context = {
        'total': total,
        'shipping_address': shipping_address,
    }
    return render(request, 'khalti.html', context)


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from io import BytesIO
from django.http import HttpResponse
from .models import Order

def generate_pdf(request, order_id):
    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)

    # Get the order details from the database.
    order = Order.objects.get(id=order_id)

    # Define the styles to use in the PDF.
    styles = {
        'title': {
            'fontName': 'Helvetica-Bold',
            'fontSize': 20,
            'leading': 24,
            'alignment': 1,
        },
        'heading': {
            'fontName': 'Helvetica-Bold',
            'fontSize': 14,
            'leading': 16,
            'alignment': 0,
        },
        'cell': {
            'fontName': 'Helvetica',
            'fontSize': 12,
            'leading': 14,
            'alignment': 0,
        },
    }

    # Define the table data to use in the PDF.
    data = [
        ['Order ID:', order.id],
        ['Order Date:', order.date_orderd.strftime('%m/%d/%Y %I:%M %p')],
        ['Order Status:', order.complete],
        ['Order Total:', '${:,.2f}'.format(order.get_cart_total)],
    ]

    # Define the table styles to use in the PDF.
    table_style = TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('LEADING', (0, 0), (-1, -1), 14),
    ])

    # Create the table and apply the styles to it.
    table = Table(data)
    table.setStyle(table_style)

    # Add the title to the PDF.
    p.setFont(styles['title']['fontName'], styles['title']['fontSize'])
    p.drawString(2.75 * inch, 10.5 * inch, 'Order Summary')

    # Add the table to the PDF.
    table.wrapOn(p, 6.5 * inch, 4.5 * inch)
    table.drawOn(p, 1.25 * inch, 9.5 * inch)

    # Close the PDF object cleanly, and we're done.
    p.shoswPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="order_{}.pdf"'.format(order.id)
    return response


