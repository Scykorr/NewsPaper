from django.urls import path
from .views import NewsList, OneNews

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', OneNews.as_view()),
]
