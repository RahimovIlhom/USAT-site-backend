from django.urls import path
from .views import get_news_list, get_news_detail

urlpatterns = [
    path('all/', get_news_list, name='get_news_list'),
    path('detail/<int:pk>/', get_news_detail, name='get_news_detail'),
]
