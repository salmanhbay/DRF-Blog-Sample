__author__ = "Salman Humdullah"
__email__ = "salman.humdullah@gmail.com"
__date__ = "6 Aug 2023"

from django.urls import path
from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, UserPostListAPIView

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),

    # Extra function
    path('my/posts/', UserPostListAPIView.as_view(), name='user-post-list'),

]