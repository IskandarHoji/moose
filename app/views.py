from django.shortcuts import render,redirect
from .models import Blog,Contact


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
    if request.method == "POST":
        data = request.POST
        full_name = data.get("full_name")
        subject = data.get("subject")
        email = data.get("email")
        message = data.get("message")
        obj = Contact.objects.create(full_name=full_name,subject=subject,email=email,message=message)
        obj.save()
        return redirect("/contact")


    return render(request, 'contact.html')
