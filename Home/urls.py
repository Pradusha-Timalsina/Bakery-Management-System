from django.urls import path
from Account.views import login_view,register_view
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.home_view,name="index"),
    path("about",views.about_view,name="about"),
    path("shop-left-sidebar",views.shop_view,name="shop"),
    path("contact",views.contact_view,name="contact"),
     path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path("my-account",views.my_account_view,name="acccount"),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]
