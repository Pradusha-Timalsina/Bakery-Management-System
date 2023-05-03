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
    path("billing/",views.billing_details,name="billing"),
    path("ordersummary/",views.orderSummary,name="ordersummary"),
    path("update_item/",views.updateItem,name="updateitem"),
    


    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

]