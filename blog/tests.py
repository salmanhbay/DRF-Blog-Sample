__author__ = "Salman Humdullah"
__email__ = "salman.humdullah@gmail.com"
__date__ = "6 Aug 2023"

from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from blog.models import Post


class UserLoginAndGetTokenTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')


    def test_user_login_and_get_token(self):
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(reverse('obtain-jwt-token'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)


class PostCRUDTestCase(TestCase):
    email = "test@example.com"
    password = "testpassword"

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="test",
            email=self.email,
            password='testpassword'
        )
        self.token = Token.objects.create(user=self.user)
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create_post(self):
        data = {
            'title': 'Test Post',
            'content': 'This is a test post content.',
            'author': self.user.id
        }
        response = self.client.post(reverse('post-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post content.', author=self.user)
        response = self.client.get(reverse('post-detail', kwargs={'pk': post.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')

    def test_update_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post content.', author=self.user)
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        data = {'title': 'Updated Post'}
        response = self.client.patch(reverse('post-detail', kwargs={'pk': post.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Post')

    def test_delete_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post content.', author=self.user)
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.delete(reverse('post-detail', kwargs={'pk': post.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)