from django.urls import path
from .views import post_create

urlpatterns = [
    path('create/', post_create, name='post_create'),
]