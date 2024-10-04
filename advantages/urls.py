from django.urls import path

from .views import GetAdvantagesListView

urlpatterns = [
    path('all/', GetAdvantagesListView.as_view(), name='get_advantages_list'),
]
