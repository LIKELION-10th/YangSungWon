from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone

def first(request):
    return render(request, 'first.html')

def hobby(request):
    return render(request, 'hobby.html')

def favplace(request):
    return render(request, 'favplace.html')

def favmusic(request):
    return render(request, 'favmusic.html')

def pic(request):
    return render(request, 'pic.html')

def profile(request):
    return render(request, 'profile.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    if (request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')
