from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from .models import Post


def index(request):
    posts = get_list_or_404(Post)
    return render(request, "blog/index.html", {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "blog/detail.html", {'post': post})
