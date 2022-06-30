from django.shortcuts import render

from Posts.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')