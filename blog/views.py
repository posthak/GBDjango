from django.shortcuts import render, get_object_or_404
from .models import Author, Post

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):

    return HttpResponse(request)

def my_view(request):
    context = {"name": "John"}
    return render(request, "blog/my_template.html", context)

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'blog/author_posts.html', {'author': author, 'posts': posts})

def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_full.html', {'post': post})
