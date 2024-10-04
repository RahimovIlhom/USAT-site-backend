from django.urls import path
from .views import basic_logout, redirect_admin

urlpatterns = [
    path('', redirect_admin, name='redirect_admin'),
    path('accounts/logout/', basic_logout, name='custom_logout'),
]
