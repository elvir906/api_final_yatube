from rest_framework import viewsets

from django.shortcuts import get_object_or_404

from posts.models import Post, Comment, Follow, Group
from .serializers import PostSerializer, CommentSerializer
from .serializers import FollowSerializer, GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        group = get_object_or_404(Group, slug=serializer.initial_data['group'])
        serializer.save(author=self.request.user, group=group)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
