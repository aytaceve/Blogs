from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import BlogForm

# Create your views here.


def home_view(request):
    posts = Blog.objects.values()
    context = {
        'posts': posts
    }
    return render(request, 'home.html', context=context)


def create_view(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'create.html', context=context)


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


def delete(request, id):
    post_to_delete = get_object_or_404(Blog, id=id)
    post_to_delete.delete()
    return redirect('home')


def single_blog_view(request, id):
    post = Blog.objects.filter(id=id)
    context = {
        'post': post
    }
    return render(request, 'single_blog.html', context=context)


def blog_post_like(request, id):
    post = get_object_or_404(Blog, id=id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove()
    else:
        post.likes.add(request.user)

    return redirect('/')

