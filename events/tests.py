from django.contrib.auth.models import User
from .models import Event
from rest_framework import status
from rest_framework.test import APITestCase


class EventListViewTests(APITestCase):
    """
    Tests for the Event model list view
    """

    def setUp(self):
        User.objects.create_user(username="superuser", password="password")

    def test_can_list_events(self):
        sophie = User.objects.get(username="superuser")
        Event.objects.create(owner=sophie, title="event title", event_date="2024-04-01")
        response = self.client.get("/events/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_out_user_cant_create_event(self):
        response = self.client.post("/events/", {"title": "a title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        count = Event.objects.count()
        self.assertEqual(count, 0)
