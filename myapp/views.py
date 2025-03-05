from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from .Books_Forms import BooksForm
from .User_form import SignupForm, ProfileUpdateForm, LoginForm, Sub_LoginForm


def home(request):
    return render(request, template_name='bmHome/home.html')

def books(request):
    genre_filter = request.GET.get('genre', None)
    if genre_filter:
        allbooks = Book.objects.filter(genre__iexact=genre_filter)
    else:
        allbooks = Book.objects.all()

    item = {
        'allbooks': allbooks,
        'genre': genre_filter,
    }
    return render(request, template_name='bmHome/books.html', context=item)

def books_details(request, book_id):
    allbooks = Book.objects.get(pk=book_id)
    context = {
        'allbooks': allbooks,
    }
    return render(request, template_name='bmHome/books_details.html', context=context)

def contacts(request):
    return render(request, template_name='bmHome/contacts.html')

def subscription(request):
    if request.method == 'POST':
        return redirect(reverse('sub_base'))
    return render(request, 'login_signup_subscription/subscription.html')


####################################################################


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'login_signup_subscription/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                authenticate(request, user)

                if user.user_type == 'normal':
                    return redirect('log_profile')
                elif user.user_type == 'shopowner':
                    return redirect('shop_profile')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login_signup_subscription/login.html', {'form': form})


def subscription(request):
    if request.method == 'POST':
        form = Sub_LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = authenticate(request, username=username, password=password)

            if user is None:
                user = authenticate(request, username=email, password=password)

            if user is not None:

                return redirect('sub_profile')
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = Sub_LoginForm()
    return render(request, 'login_signup_subscription/subscription.html', {'form': form})


def forget_pass(request):
    return render(request, template_name='login_signup_subscription/forget_pass.html')

def payment(request):
    return render(request, template_name='login_signup_subscription/payment.html')
def process_payment(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        transaction_id = request.POST.get('transaction_id')
        amount = request.POST.get('amount')

        if phone and transaction_id and amount:
            messages.success(request, "Payment processed successfully!")
            return redirect('payment')
        else:
            messages.error(request, "Invalid payment details. Please try again.")
            return redirect('payment')

    return redirect('payment')

#######################################################################################
def log_base(request):
    return render(request, template_name='login_user/log_base.html')
def log_navbar(request):
    return render(request, template_name='login_user/log_navbar.html')
def log_book(request):
    genre_filter = request.GET.get('genre', None)
    if genre_filter:
        allbooks = Book.objects.filter(genre__iexact=genre_filter)
    else:
        allbooks = Book.objects.all()

    item = {
        'all_books': allbooks,
        'genre': genre_filter,
    }
    return render(request, template_name='login_user/log_book.html', context=item)
def log_books_details(request, book_id):
    allbooks = Book.objects.get(id=book_id)
    context = {
        'allbooks': allbooks,
    }
    return render(request, template_name='login_user/log_books_details.html', context=context)
@login_required
def purchase_book(request, book_id):
    user = request.user

    if hasattr(user, 'profile'):
        user_profile = user.profile
    else:
        user_profile = None

    book = get_object_or_404(Book, pk=book_id)

    if book.stock_quantity > 0:

        order = Order.objects.create(
            user_id=request.user,
            book_name=book,
            amount=book.price,
            status='buy',
            phone=request.user.profile.phone
        )

        book.stock_quantity -= 1
        book.save()

        return render(request, 'purchase_success.html', {'order': order})
    else:
        return render(request, 'purchase_failed.html', {'message': 'Out of stock'})
def confirm_payment(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'login_user/confirm_payment.html',{'book': book})
def process_payment_for_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        phone = request.POST.get('phone')
        transaction_id = request.POST.get('transaction_id')
        amount = request.POST.get('amount')

        if phone and transaction_id and amount:

            book.is_sold = True
            book.save()
            messages.success(request, f"Payment successful for {book.book_name}. Transaction ID: {transaction_id}.")
            return redirect('payment_confirmation', book_id=book.id)
        else:
            messages.error(request, "Please provide all the required details.")
            return redirect('process_payment', book_id=book.id)

    return render(request, 'login_user/process_payment_for_book.html', {'book': book})
def payment_confirmation(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'login_user/payment_confirmation.html', {'book': book})
def log_help(request):
    return render(request, template_name='login_user/log_help.html')
@login_required
def log_profile(request):
    return render(request, 'login_user/log_profile.html', {'user': request.user})
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('log_profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'login_user/profile_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


