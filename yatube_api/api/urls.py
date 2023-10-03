from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostsViewSet
)


routers = DefaultRouter()
routers.register('posts', PostsViewSet, basename='posts')
routers.register('groups', GroupViewSet, basename='groups')
routers.register('follow', FollowViewSet, basename='follow')
routers.register(r'posts/(?P<post_id>\d+)/comments',
                 CommentViewSet,
                 basename='comments')

urlpatterns = [
    path('v1/', include(routers.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))

]
