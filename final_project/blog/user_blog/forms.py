from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        exclude = ['author']
        
class RegisterForm(UserCreationForm):
    email = models.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 