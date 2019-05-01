from django.shortcuts import render
from .models import Post, User

# Create your views here.
def list(request, user_id):
    posts=Post.objects.all()
    return render(request,'list.html',{'posts':posts, 'users':users})
    
def create(request):
    return render(request,'create.html',)