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
from django.contrib import admin
from django.urls import path

from myapp import views as myapp_views
from myapp import views as login_signup_subscription

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
]
