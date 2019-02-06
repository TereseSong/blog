from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from datetime import datetime
from django.urls import reverse

def hello_world(request):
    return render(request,'hello_world.html',{'current_time': datetime.now()})


def index(request):
    return HttpResponse("Hello,world!")

def home(request):
    post_list = Post.objects.all()
    return render(request,'home.html',{'post_list': post_list})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})