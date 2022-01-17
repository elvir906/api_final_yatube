from rest_framework import viewsets
from rest_framework import filters
from rest_framework import permissions
from rest_framework.pagination import LimitOffsetPagination

from django.shortcuts import get_object_or_404

from posts.models import Post, Follow, Group
from .serializers import PostSerializer, CommentSerializer
from .serializers import FollowSerializer, GroupSerializer
from .permission import IsAuthorOrReadOnlyPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    filter_backends = (filters.OrderingFilter,)
    pagination_class = LimitOffsetPagination
    ordering_fields = ('pub_date',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('=following__username',)
    ordering_fields = ('user',)

    def get_queryset(self):
        return self.request.user.followings.all()
