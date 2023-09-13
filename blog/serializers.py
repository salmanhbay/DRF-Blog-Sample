__author__ = "Salman Humdullah"
__email__ = "salman.humdullah@gmail.com"
__date__ = "6 Aug 2023"

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class EmailTokenObtainSerializer(TokenObtainSerializer):
    username_field = User.EMAIL_FIELD


class CustomTokenObtainPairSerializer(EmailTokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data