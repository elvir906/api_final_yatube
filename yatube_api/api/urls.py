from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register(
    'follow',
    FollowViewSet,
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
