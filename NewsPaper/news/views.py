from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'