from django.urls import path
from .views import post_create, feed, like_post

urlpatterns = [
    path('create/', post_create, name='post_create'),
    path('feed/', feed, name='feed'),
    path('like/', like_post, name='like')
]