import datetime

from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .filters import NewsFilter
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


class NewsSearch(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.datetime.now(datetime.UTC)
        context['filterset'] = self.filterset
        return context
