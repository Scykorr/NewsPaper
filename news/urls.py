from django.urls import path
from .views import NewsList, OneNews, NewsSearch

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', OneNews.as_view()),
    path('search/', NewsSearch.as_view()),
]
