from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name='bmHome/home.html')

def books(request):
    return render(request, template_name='bmHome/books.html')

def books_details(request):
    return render(request, template_name='bmHome/books_details.html')

def contacts(request):
    return render(request, template_name='bmHome/contacts.html')

def forget_pass(request):
    return render(request, template_name='login_signup_subscription/forget_pass.html')

def login(request):
    return render(request, template_name='login_signup_subscription/login.html')

def payment(request):
    return render(request, template_name='login_signup_subscription/payment.html')

def signup(request):
    return render(request, template_name='login_signup_subscription/signup.html')

def subscription(request):
    return render(request, template_name='login_signup_subscription/subscription.html')