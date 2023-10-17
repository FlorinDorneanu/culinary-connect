from django.shortcuts import render
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer



class EventList(APIView):
    serializer_class = EventSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(
            events, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )