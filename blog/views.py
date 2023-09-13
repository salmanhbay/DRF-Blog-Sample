__author__ = "Salman Humdullah"
__email__ = "salman.humdullah@gmail.com"
__date__ = "6 Aug 2023"

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    # - create model named Post and create endpoints to let the user create post
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# update post, get single post, get all posts and delete post.
class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


# Extra feature to get all posts of a particular user
class UserPostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


# # Use TokenObtainPairView for login
# class ObtainJWTWithEmailView(TokenObtainPairView):
#     pass

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Use TokenRefreshView for token refresh
class RefreshJWTTokenView(TokenRefreshView):
    pass


# Use TokenVerifyView for token verification
class VerifyJWTTokenView(TokenVerifyView):
    pass
