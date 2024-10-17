from django.urls import path
from .views import GetNewsListView, GetDetailNewsView, CategoryListWithNewsView, CategoryRelatedNewsListView

urlpatterns = [
    path('categories/', CategoryListWithNewsView.as_view(), name='get_categories_list'),
    path('categories/<slug:slug>/', CategoryRelatedNewsListView.as_view(), name='get_category_related_news_list'),
    path('all/', GetNewsListView.as_view(), name='get_news_list'),
    path('detail/<slug:slug>/', GetDetailNewsView.as_view(), name='get_news_detail'),
]
