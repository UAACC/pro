from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, AuthorViewSet, CommentViewSet
from .views import PostList, PostDetail, UpdatePost, PostCreate, DeletePost, FriendRequestViewSet
from .views import get_comment, post_comment, update_comment, delete_comment
from .views import get_comment_like, post_comment_like, delete_comment_like
from .views import get_post_like, post_post_like, delete_post_like
from .views import create_request, accept_request
from . import views
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('authors', AuthorViewSet)
router.register('friend_requests', FriendRequestViewSet)
router.register('comments', CommentViewSet)
# router.register('likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Post
    path('posts/<int:pk>/', PostDetail.as_view()),#router?
    path('posts/<int:pk>/edit', UpdatePost.as_view()),
    path('posts/create', PostCreate.as_view()),
    path('posts/<int:pk>/delete', DeletePost.as_view()),
    path('posts/', PostList.as_view()),

    # Friend Requests
    path('create_request/<int:userID>/', create_request, name = 'send friend request'),
    path('accept_request/<int:requestID>/', accept_request, name = 'accept friend request'),

    # Comments
    path('comments/get_comment/<int:postId>/', get_comment, name="get_comment"),
    path('comments/post_comment/<int:postId>/', post_comment, name="post_comment"),
    path('comments/update_comment/<int:postId>/', update_comment, name="update_comment"),
    path('comments/delete_comment/<int:postId>/', delete_comment, name="delete_comment"),

    # Likes
    path('likes/get_comment_like/<int:commentId>/', get_comment_like, name="get_comment_like"),
    path('likes/post_comment_like/<int:commentId>/', post_comment_like, name="post_comment_like"),
    path('likes/delete_comment_like/<int:commentId>/', delete_comment_like, name="delete_comment_like"),
    path('likes/get_post_like/<int:postId>/', get_post_like, name="get_post_like"),
    path('likes/post_post_like/<int:postId>/', post_post_like, name="post_post_like"),
    path('likes/delete_post_like/<int:postId>/', delete_post_like, name="delete_post_like"),
]
