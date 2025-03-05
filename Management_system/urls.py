"""
URL configuration for Management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import settings
from django.conf.urls.static import static

from myapp import views as myapp_views
from myapp import views as login_signup_subscription
from myapp import views as login_user
from myapp import views as subscribed_user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp_views.home, name='home'),
    path('contacts/', myapp_views.contacts, name='contacts'),
    path('books/', myapp_views.books, name='books'),
    path('books_details/', myapp_views.books_details, name='books_details'),

    path('login/', login_signup_subscription.login, name='login'),
    path('signup/', login_signup_subscription.signup, name='signup'),
    path('subscription/', login_signup_subscription.subscription, name='subscription'),
    path('forget_pass/', login_signup_subscription.forget_pass, name='forget_pass'),
    path('payment/', login_signup_subscription.payment, name='payment'),
    path('process-payment/', login_signup_subscription.process_payment, name='process_payment'),

    path('log_base/', login_user.log_base, name='log_base'),
    path('log_navbar/', login_user.log_navbar, name='log_navbar'),
    path('log_book/', login_user.log_book, name='log_book'),
    path('log_books_details/<int:book_id>', login_user.log_books_details, name='log_books_details'),
    path('log_help/', login_user.log_help, name='log_help'),
    path('log_profile/', login_user.log_profile, name='log_profile'),
    path('logout/', login_user.logout_view, name='logout'),
    path('update_profile/', login_user.update_profile, name='update_profile'),
    path('purchase_book/<int:book_id>/purchase/', login_user.purchase_book, name='purchase_book'),
    path('confirm_payment/<int:book_id>/', login_user.confirm_payment, name='confirm_payment'),
    path('process-payment/<int:book_id>/', login_user.process_payment_for_book,name='process_payment_for_book'),
    path('payment_confirmation/<int:book_id>/', login_user.payment_confirmation,name='payment_confirmation'),




] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

