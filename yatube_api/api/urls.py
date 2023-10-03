from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostsViewSet
)


routers_v1 = DefaultRouter()
routers_v1.register('posts', PostsViewSet, basename='posts')
routers_v1.register('groups', GroupViewSet, basename='groups')
routers_v1.register('follow', FollowViewSet, basename='follow')
routers_v1.register(r'posts/(?P<post_id>\d+)/comments',
                    CommentViewSet,
                    basename='comments')

urlpatterns = [
    path('v1/', include(routers_v1.urls)),
    path('v1/', include('djoser.urls.jwt'))

]
