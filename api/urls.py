from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, AuthorViewSet, CommentViewSet, LikeViewSet,PostList,PostDetail,UpdatePost,PostCreate,DeletePost,CategoryDetail,CategoryList#PostSearchList
from . import views



router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('authors', AuthorViewSet)


router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),

    #############POST URLS#################################################################
    path('posts/<int:pk>/', PostDetail.as_view()),#router?
    path('posts/<int:pk>/edit', UpdatePost.as_view()),
    path('posts/create', PostCreate.as_view()),
    path('posts/<int:pk>/delete', DeletePost.as_view()),
    path('posts/', PostList.as_view()),
    #path('posts/search', PostSearchList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('categories/', CategoryList.as_view()),


]
