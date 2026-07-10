from django.db import models
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

User = get_user_model()
# Create your models here.
class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=300,label='username')
    widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
               'password': forms.PasswordInput(attrs={'class': 'form-control'})
               }
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=300,label='username')
    password = forms.CharField(label='password')
    widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
               'password': forms.PasswordInput(attrs={'class': 'form-control'})
               }