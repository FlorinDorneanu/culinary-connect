
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    """
    Retrieve events from DB.
    Create new events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        """
        Check for user authentication.
        """
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]

    filterset_fields = {
        'owner__followed__owner__profile': ['exact'],
        'owner__profile': ['exact'],
        'category': ['exact'],
        'event_date': ['lte'],
    }

    search_fields = [
        'owner__username',
        'title',
        'city',
        'country',
    ]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update & Destroy events.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all()