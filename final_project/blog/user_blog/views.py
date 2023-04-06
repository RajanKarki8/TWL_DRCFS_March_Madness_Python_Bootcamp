from django.shortcuts import render
from . models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def home_view(request):
    blogs = BlogPost.objects.all()
    context = {'blogs':blogs}
    return render(request, 'user_blog/home.html', context)

def createBlog(request):
    form = BlogForm
    context = {'form':form}
    return render(request, 'user_blog/create_blog.html', context)

