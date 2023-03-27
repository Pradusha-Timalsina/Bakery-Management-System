from django.urls import path
from Account.views import login_view,register_view
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.home_view,name="index"),
    path("about",views.about_view,name="about"),
    path("shop-left-sidebar",views.shop_view,name="shop"),
    path("contact",views.contact_view,name="contact"),
    path("product",views.product_view,name="product"),

    path("my-account",views.my_account_view,name="acccount"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="forgot.html"),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="resettext.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="resetdone.html"),name="password_reset_complete"),
]
