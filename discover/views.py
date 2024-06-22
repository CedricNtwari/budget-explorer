from django.shortcuts import render
from django.views import generic
from .models import Post, Comment, Favorite

# Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = 'discover/discover_list.html'