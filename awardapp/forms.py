from requests import request
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'

class VotesForm(forms.ModelForm):
    class Meta:
        model=Votes
        fields='__all__'

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','password1','password2')

class LoginForm(forms.ModelForm):
    class Meta:
        model= Login
        fields ='__all__'