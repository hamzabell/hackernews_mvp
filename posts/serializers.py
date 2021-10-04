from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'upvotes_count': {
                'read_only': True
            }
        }


class UpVoteSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()