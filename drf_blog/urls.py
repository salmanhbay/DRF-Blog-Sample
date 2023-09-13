__author__ = "Salman Humdullah"
__email__ = "salman.humdullah@gmail.com"
__date__ = "6 Aug 2023"

from django.contrib import admin
from django.urls import path, include
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from blog.views import EmailTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('auth/token/', EmailTokenObtainPairView.as_view(), name='obtain-jwt-token'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='refresh-jwt-token'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='verify-jwt-token'),

    # This one function is extra to fetch all posts of a logged in user.
    path('api/blog/', include('blog.urls')),
]