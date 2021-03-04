from rest_framework import viewsets, status,generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly#update/retrive
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, AuthorSerializer, PostSerializer, CommentSerializer,UpdateSerializer,PostCreateSerializer, FriendRequestSerializer
from .models import Author, Post, FriendRequest
from django.http import HttpResponse
from .permissions import IsOwnerOrReadOnly
User = get_user_model()

# user and author
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


# Like & Comment
# class LikeViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = LikeSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (IsAuthenticated, )


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

def get_comment(request, postId):
    # get comments id from post
    post = Post.objects.get(id=postId)
    commentIds = post.comments

    # get comments by id
    comments = []
    for commentId in commentIds:
        comments.append(Comment.objects.get(id=commentId))

    return HttpResponse(comments)

def post_comment(request, postId):
    post = Post.objects.get(id=postId)
    # create commen
    # save comment

    return HttpResponse()

def update_comment(request, postId):
    return HttpResponse()

def delete_comment(request, postId):
    return HttpResponse()

def get_comment_like(request, commentId):
    return HttpResponse()

def post_comment_like(request, commentId):
    return HttpResponse()

def delete_comment_like(request, commentId):
    return HttpResponse()

def get_post_like(request, postId):
    return HttpResponse()

def post_post_like(request, postId):
    return HttpResponse()

def delete_post_like(request, postId):
    return HttpResponse()


# Post
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )


class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def create_view(self, serializer):
        serializer.save(authorId = self.request.user)


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )


class UpdatePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class DeletePost(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )


# Friend Request

class FriendRequestViewSet(viewsets.ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    

def create_request(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = FriendRequest.objects.get_or_create(
        from_user = from_user, to_user = to_user)
    if created:
        return HttpResponse('Friend request sent')
    else:
        return HttpResponse('Friend request not accepted')



def accept_request(request, requestID):
    friend_request = FriendRequest.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('Friend request accepted.')
