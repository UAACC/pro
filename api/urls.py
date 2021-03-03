from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, AuthorViewSet, PostViewSet, CommentViewSet, LikeViewSet,UpdateViewSet,DeleteViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('authors', AuthorViewSet)
router.register('posts', PostViewSet)
router.register('update', UpdateViewSet)
router.register('delete', DeleteViewSet)
router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
