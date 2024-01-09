from django.urls import path
from django.views.decorators.cache import cache_page

from .views import NewsList, OneNews, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, ArticleCreate, ArticleUpdate, \
    ArticleDelete, subscriptions

urlpatterns = [
    path('', cache_page(60)(NewsList.as_view()), name='post_list'),
    path('<int:pk>', cache_page(300)(OneNews.as_view()), name='post_detail'),
    path('search/', NewsSearch.as_view(), name='post_search'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),


]
