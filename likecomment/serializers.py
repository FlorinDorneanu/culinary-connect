from rest_framework import serializers
from likecomment.models import LikeComment


class LikeCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the LikeComment model
    The create method handles the unique constraint on 'owner' and 'comment'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = LikeComment
        fields = ['id', 'created_at', 'owner', 'comment']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })