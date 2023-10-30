from django.contrib.auth.models import User
from .models import Post
from .models import Like
from rest_framework import status
from rest_framework.test import APITestCase


class LikeListViewTests(APITestCase):
    """
    Tests for the Like model list view
    """

    def setUp(self):
        superuser = User.objects.create_user(username="superuser", password="password")
        post_a = Post.objects.create(owner=superuser, content="a post")

    def test_can_list_like(self):
        superuser = User.objects.get(username="superuser")
        post_a = Post.objects.get(id=1)
        Like.objects.create(owner=superuser, post=post_a)
        response = self.client.get("/likes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LikeDetailViewTests(APITestCase):
    """
    Tests for the Like model detail view
    """

    def setUp(self):
        superuser = User.objects.create_user(username="superuser", password="password")
        superuser1 = User.objects.create_user(username="superuser1", password="password")
        post_a = Post.objects.create(owner=superuser, content="a post")
        post_b = Post.objects.create(owner=superuser1, content="another post")
        Like.objects.create(owner=superuser, post=post_a)
        Like.objects.create(owner=superuser1, post=post_b)

    def test_cant_retrieve_like_using_invalid_id(self):
        response = self.client.get("/likes/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_can_retrieve_like_using_valid_id(self):
        response = self.client.get("/likes/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
