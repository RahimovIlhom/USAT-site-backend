from django.urls import path
from .views import GetNewsListView, GetDetailNewsView

urlpatterns = [
    path('all/', GetNewsListView.as_view(), name='get_news_list'),
    path('detail/<int:pk>/', GetDetailNewsView.as_view(), name='get_news_detail'),
]
