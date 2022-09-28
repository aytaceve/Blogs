from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

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


def delete_likes(request, pk):
    post = get_object_or_404(Blog, id=request.POST.get('post_id'))
    user_liked = post.likes.values('id')
    for user in user_liked:
        post.likes.remove(user['id'])
    print(user_liked)

    return HttpResponseRedirect(reverse('single_blog', args=[str(pk)]))