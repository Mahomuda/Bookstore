from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )
####################################################################
class SignupForm(UserCreationForm):
   username = forms.CharField(
       widget=forms.TextInput(
           attrs={
               'class':
                   'form-control'
           }
       )
   )
   password1 = forms.CharField(
       widget=forms.PasswordInput(
           attrs={
               'class':
                   'form-control'
           }
       )
   )
   password2 = forms.CharField(
       widget=forms.PasswordInput(
           attrs={
               'class':
                   'form-control'
           }
       )
   )
   email = forms.CharField(
       widget=forms.TextInput(
           attrs={
               'class':
                   'form-control'
           }
       )
   )

   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2','user_type']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
           model = User
           fields = ['username', 'email', 'address', 'contact_number']

class Sub_LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
