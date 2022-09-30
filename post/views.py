from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import *
from .forms import BlogForm, NewUserForm

# Create your views here.


def register_view(request):
    if request.method == "POST":
        print('POOOOOSSSTTTTT----', request.POST)
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect("home")
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    context = {'register_form': form}
    return render(request, 'register.html', context=context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in {username}')
                return redirect('home')

            else:
                messages.info(request, 'Username or password is incorrect.')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')

@login_required
def home_view(request):
    posts = Blog.objects.values()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context=context)

@login_required
def create_view(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'create.html', context=context)

@login_required
def update_view(request, id):
    post = get_object_or_404(Blog, id=id)
    form = BlogForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'update.html', context=context)

@login_required
def delete(request, id):
    post_to_delete = get_object_or_404(Blog, id=id)
    post_to_delete.delete()
    return redirect('home')

@login_required
def single_blog_view(request, id):
    # post = Blog.objects.filter(id=id).first()
    post = get_object_or_404(Blog, id=id)
    total_likes = post.total_likes()
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    context = {
        'post': post
    }
    context['total_likes'] = total_likes
    context['liked'] = liked
    return render(request, 'single_blog.html', context=context)

@login_required
def like_view(request, pk):
    post = get_object_or_404(Blog, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        print('REQUQUWUSUSU USERER-------', request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('single_blog', args=[str(pk)]))

@login_required
def delete_likes(request):
    ids = []
    blogs = Blog.objects.values()
    print('blogs111111', blogs)
    for i in range(blogs.count()):
        ids.append(blogs[i]['id'])

    print('idss22222222', ids)

    for id in ids:
        post = get_object_or_404(Blog, id=id)
        print('post333333333', type(post))
        user_liked = post.likes.values('id')
        for user in user_liked:
            post.likes.remove(user['id'])

    return redirect('home')