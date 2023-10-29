from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likecomment.models import LikeComment
from likecomment.serializers import LikeCommentSerializer


class LikeCommentList(generics.ListCreateAPIView):
    """
    List comment likes or create a comment like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeCommentDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a comment like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeCommentSerializer
    queryset = LikeComment.objects.all()
