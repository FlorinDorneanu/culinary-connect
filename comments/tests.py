from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from rest_framework import status
from rest_framework.test import APITestCase


class CommentsListViewTests(APITestCase):
    """
    Tests for the Comment model list view
    """

    def setUp(self):
        superuser = User.objects.create_user(username="superuser", password="password")
        a_post = Post.objects.create(owner=superuser, description="a post")

    def test_can_list_comments(self):
        superuser = User.objects.get(username="superuser")
        a_post = Post.objects.get(id=1)
        Comment.objects.create(owner=superuser, post=a_post, content="a comment")
        response = self.client.get("/comments/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_comment(self):
        a_post = Post.objects.get(id=1)
        response = self.client.post(
            "/comments/", {"post": a_post, "content": "comment"}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Comment.objects.count()
        self.assertEqual(count, 0)

    def test_logged_in_user_can_post_comment(self):
        self.client.login(username="superuser", password="password")
        a_post = Post.objects.get(id=1)
        current_user = User.objects.get(username="superuser")
        response = self.client.post(
            "/comments/", {"owner": current_user, "post": 1, "content": "comment"}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)