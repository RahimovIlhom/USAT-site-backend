from django.urls import path

from .views import get_advantages_list

urlpatterns = [
    path('all/', get_advantages_list, name='get_advantages_list'),
]
