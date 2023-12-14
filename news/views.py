from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    queryset = Post.objects.all().order_by('-create_date')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10


class OneNews(DetailView):
    model = Post
    template_name = 'news_one.html'
    context_object_name = 'news_one'
    pk_url_kwarg = 'pk'
