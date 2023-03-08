from django.shortcuts import render
from .models import Blog


def home_view(request):
    posts = Blog.objects.filter(is_published =True)
    context = {
        'posts': posts
    }
    return render(request, 'index.html',context)


def blog_view(request):
    posts = Blog.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog.html',context)

def blog_detail_view(request, pk):
    post = Blog.objects.get(id = pk)
    context = {
        'post': post
    }
    return render(request, 'blog-single.html',context)


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')
