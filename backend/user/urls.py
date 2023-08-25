from django.urls import path

from . views import create_auth

urlpatterns = [
    path('signup/', create_auth)
]