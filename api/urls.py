from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, AuthorViewSet, CommentViewSet, \
    LikeViewSet,PostList,PostDetail,UpdatePost,PostCreate,DeletePost, \
    create_request, accept_request
from . import views
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('authors', AuthorViewSet)

# router.register('friend_requests', FriendRequestViewSet)

router.register('comments', CommentViewSet)
router.register('likes', LikeViewSet)

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
    path('accept_request/<int:requestID>/', accept_request, name = 'accept friend request')
    # path('friend_requests/create_request/<int:userID>/', FriendRequestViewSet.as_view()),
    # path('friend_requests/accept_request/<int:requestID>/', FriendRequestViewSet.as_view())

]
