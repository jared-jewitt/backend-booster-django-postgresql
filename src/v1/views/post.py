from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from src.v1.models.post import Post
from src.v1.serializers.post import PostSerializer


class PostModelViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)

        return Response(serializer.data)
