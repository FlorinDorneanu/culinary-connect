
from django.db import models
from django.contrib.auth.models import User
from datetime import *
from taggit.managers import TaggableManager

EVENT_CATEGORIES = (
    ("Recipe Share", "Recipe Share"),
    ("Cooking Challenge", "Cooking Challenge"),
    ("Food Photography", "Food Photography"),
    ("Restaurant Review", "Restaurant Review"),
    ("Cooking Tips", "Cooking Tips"),
    ("Food Event", "Food Event"),
    ("Culinary Workshop", "Culinary Workshop"),
    ("Other", "Other"),
)


class Event(models.Model):
    """
    Event model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    event_date = models.DateField(blank=False)
    event_time = models.TimeField(blank=True, null=True)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    tags = TaggableManager(blank=True)
    category = models.CharField(
        max_length=50, choices=EVENT_CATEGORIES, default='Other'
    )
    image = models.ImageField(
        upload_to='images/', default='../default_post_tiwu5f', blank=True
    )

    class Meta:
        """
        Order events by date of event.
        """
        ordering = ['-event_date']

    def __str__(self):
        return f'{self.id} {self.title}'
