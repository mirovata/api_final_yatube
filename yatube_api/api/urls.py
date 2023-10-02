from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from api.views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostsViewSet)


routers = DefaultRouter()
routers.register('posts', PostsViewSet, basename='posts')
routers.register('groups', GroupViewSet, basename='groups')
routers.register('follow', FollowViewSet, basename='follow')
routers.register(r'posts/(?P<post_id>\d+)/comments',
                 CommentViewSet,
                 basename='comments')

urlpatterns = [
    path('v1/', include(routers.urls)),
    path('v1/jwt/create/', TokenObtainPairView.as_view()),
    path('v1/jwt/refresh/', TokenRefreshView.as_view()),
    path('v1/jwt/verify/', TokenVerifyView.as_view())
]
