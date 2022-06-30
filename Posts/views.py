from django.shortcuts import render, HttpResponseRedirect

from Posts.models import Post
from .forms import PostForm

def newpost(request):
    return render(request, 'Posts/newpost.html')

def view_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'Posts/view_post.html', {'post': post})

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    return render(request, "posts/newpost.html", {'form': form})

def edit_post(request, slug):
    if request.method == 'POST':
        post = Post.objects.get(slug=slug)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        post = Post.objects.get(slug=slug)
        form = PostForm(instance=post)
    return render(request, "posts/edit_post.html", {'form': form, 'post': post})

def delete_post(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect("/") #figure out exactly what this line does

    return render(request, 'Posts/delete_post.html', {'post': post})