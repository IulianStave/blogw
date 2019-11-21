"""
Create a form that inherits from UserCreationForm
and add email field named 'email' to the default UserCreationForm

"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    #the default argumentfor the EmailFiled method argument is required = true 
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']