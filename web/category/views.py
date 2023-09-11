from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User

def Ttt(request):
    books = Book.objects.all().order_by('-id')

    ctx = {
        'books':books
    }
    return render(request, "index.html", ctx)

def Blogg(request):
    blog = Blog.objects.all().order_by('-id')

    ctt = {
        'blog':blog
    }
    return render(request, "blog_detail.html", ctt)

