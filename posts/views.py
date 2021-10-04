from django.core.checks import messages
from rest_framework import generics
from rest_framework.response import Response

from posts.models import Post
from .serializers import PostSerializer, UpVoteSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpVoteAPIView(generics.GenericAPIView):
    serializer_class = UpVoteSerializer

    def post(self, request, format=None):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        post_id = serializer.data['post_id']
        post= Post.objects.filter(pk=post_id).first()

        if  post:
            post.upvotes_count += 1
            post.save()
            return Response({
                'message': 'Post has been sucessfully upvoted'
            })


        return Response({
            "message": "Post does not exist"
        })

        