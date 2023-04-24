from django.shortcuts import render,redirect
from . models import BlogPost, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BlogForm, RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def home_view(request):
    blogs = BlogPost.objects.all() 
    context = {'blogs':blogs}
    return render(request, 'user_blog/home.html', context)

@login_required()
def createBlog(request):
    
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(request, 'Blog is added successfully!..')
            return redirect('home')
    else:
        form = BlogForm()
    context = {'form':form}
    return render(request, 'user_blog/create_blog.html', context)

def detail_view(request, pk):
    blog = BlogPost.objects.get(id = pk)
    comments  = blog.comment_set.all()
    if request.method == 'POST':
        comment = Comment.objects.create(
            user = request.user,
            blog = blog,
            body =  request.POST.get('body')
            
        )
        return redirect('blog-detail', pk = blog.id)
       
    context = {'blog':blog, 'comments':comments}
    messages.info(request, 'Login to Update and delete your blog..!')
    return render(request, 'user_blog/blog-detail.html', context)

def update_view(request,pk):
    room = BlogPost.objects.get(id = pk)
 
    
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, f'{room} is updated successfully!..')
            return redirect('home')
    else:
        form = BlogForm(instance=room)
    context = {'form':form,'room':room}
    return render(request, 'user_blog/create_blog.html', context)

def delete_view(request, pk):
    item = BlogPost.objects.get(id = pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request,  f'{item} deleted successfully..')
        return redirect('home')
    else:
        context = {'item':item}
    return render(request, 'user_blog/delete.html', context)

def UserRegister(request):
    
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account is created.')
            return redirect('home')
        
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request, 'user_blog/register.html', context)

def user_login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'user does not exit')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()    
    context = {'form':form}
    return render(request, 'user_blog/login.html', context)

def user_logout(request):
   
    logout(request)
    messages.info(request, 'logout is happened !')
    return redirect('home')
    