from django.contrib import admin
from django.urls import path, include

from .views import CreateUserView, login_view

urlpatterns = [
    path('signup/', CreateUserView.as_view()),
    path('login/', login_view),
]