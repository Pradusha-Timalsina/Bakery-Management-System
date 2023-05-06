from django.urls import include, path
from . import views
from accounts.views import login_view,register_view,logout_view

urlpatterns = [
    path("",views.home,name="index"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("shop/",views.shop,name="shop"),
    path('shop/<str:category>/', views.product_list, name='product_list'),
    path("shop/<int:product_id>",views.product_detail,name="product"),
    path("account/",views.account,name="acccount"),
    path("cart/",views.cart ,name="cart"),

    path("billing/",views.billingDetails,name="billing"),
    path("ordersummary/",views.orderSummary,name="ordersummary"),
    path("update_item/",views.updateItem,name="updateitem"),

    path("payment/",views.payment,name="payment"),
    path('payment/success/', views.payment_success, name='payment_success'),

    path('khalti-request',views.khalti_payment,name="khalti"),

    path('generate-pdf/<int:order_id>/', views.generate_pdf, name='generate_pdf'),


    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

]