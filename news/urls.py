from django.urls import path
from .views import GetNewsListView, GetDetailNewsView

urlpatterns = [
    path('all/', GetNewsListView.as_view(), name='get_news_list'),
    path('detail/<slug:slug>/', GetDetailNewsView.as_view(), name='get_news_detail'),
]
