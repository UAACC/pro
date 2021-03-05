from rest_framework import viewsets, status,generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly#update/retrive
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, AuthorSerializer, PostSerializer, CommentSerializer, LikeSerializer,UpdateSerializer,PostCreateSerializer, FriendRequestSerializer
from .models import Author, Post, FriendRequest
from django.http import HttpResponse, JsonResponse
from .permissions import IsOwnerOrReadOnly
import logging

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
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Post.postobjects.all()
    serializer_class = LikeSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Post.postobjects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


# Post
class PostList(generics.ListAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )


class PostCreate(generics.CreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    
    def create_view(self, serializer):
        serializer.save(authorId = self.request.user)


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )


class UpdatePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = UpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class DeletePost(generics.DestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )


# Friend Request
class FriendRequestViewSet(viewsets.ModelViewSet):
    serializer_class = FriendRequestSerializer
    queryset = FriendRequest.objects.all()

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        return super(FriendRequestViewSet, self).get_permissions()

    def create(self, request, *args, **kwargs):
    # create friend request
        from_user_id = Author.objects.get(id=request.data["from_user"])
        to_user_id = Author.objects.get(id=request.data["to_user"])

        if FriendRequest.objects.filter(from_user=from_user_id, to_user=to_user_id, status="R").exists():
        # Check if the request alreay exists and status is "requested".
            return Response("Unable to send friend request because the friend request alreay exists!")
        elif FriendRequest.objects.filter(from_user=from_user_id, to_user=to_user_id, status="A").exists():
        # Check if the request exists and status is "A"
            return Response("Unable to send friend request because you have already become friends!")
        elif FriendRequest.objects.filter(from_user=from_user_id, to_user=to_user_id, status="D").exists():
        # If your reuqest was declined and send again
            FriendRequest.objects.update(from_user=from_user_id, to_user=to_user_id, status='R')
            return Response("Successfully create the friend request!")

        elif FriendRequest.objects.filter(from_user=to_user_id, to_user=from_user_id, status="R").exists():
        # if he already send the request to you and status is R, then you become friend automatically
            FriendRequest.objects.update(from_user=to_user_id, to_user=from_user_id, status='A')
            return Response("He/She had sent the request to you and you become friend automatically!")
        elif FriendRequest.objects.filter(from_user=to_user_id, to_user=from_user_id, status="A").exists():
            return Response("Unable to send friend request because you have already become friends!")
        elif FriendRequest.objects.filter(from_user=to_user_id, to_user=from_user_id, status="D").exists():
            FriendRequest.objects.update(from_user=to_user_id, to_user=from_user_id, status='R')
            return Response("Successfully create the friend request!")

        else:
            friend_request = FriendRequest.objects.create(from_user=from_user_id, to_user=to_user_id, status='R')
            return Response("Successfully create the friend request!")
        
    def accept_incoming_request(self, request, *args, **kwargs):
    # accept incoming friend request
        request_from_user_id = Author.objects.get(id=request.data["from_user"])
        current_user_id = Author.objects.get(id=request.data["to_user"])
        if FriendRequest.objects.filter(from_user=request_from_user_id, to_user=current_user_id, status='A').exists():
        # Check if the request has already been accepted
            return Response("Unable to accept, because you had already accepted it!")
        elif FriendRequest.objects.filter(from_user=request_from_user_id, to_user=current_user_id, status='D').exists():
        # Check if the request has already been declined
            return Response("Unable to accept, because you had already declined it!")
        elif FriendRequest.objects.filter(from_user=request_from_user_id, to_user=current_user_id, status='R').exists():
        # If request exists and status is Requested, then able to accept:
            FriendRequest.objects.update(from_user=request_from_user_id, to_user=current_user_id, status='A')
            return Response("Successfully accept the friend request!")
        else:
            return Response("Unable to accept because this request does not exist.")
        
    def decline_incoming_request(self, request, *args, **kwargs):
    # decline incoming friend request
        request_from_user_id = Author.objects.get(id=request.data["from_user"])
        current_user_id = Author.objects.get(id=request.data["to_user"])
        if FriendRequest.objects.filter(from_user=request_from_user_id, to_user=current_user_id, status='A').exists():
        # Check if the request has already been accepted
            return Response("Unable to decline because you had already accepted it!")
        elif FriendRequest.objects.filter(from_user=request_from_user_id, to_user=current_user_id, status='D').exists():
        # Check if the request has already been delined
            return Response("Unable to decline because you had already declined it!")
        elif FriendRequest.objects.filter(from_user=request_from_user_id, to_user=current_user_id, status='R').exists():
        # Successfully decline this friend request
            FriendRequest.objects.update(from_user=request_from_user_id, to_user=current_user_id, status='D')
            return Response("Successfully decline this friend request!")
        else:
        # Request does not exist
            return Response("Unable to decline because this request does not exist.")
    
    def delete(self, request, *args, **kwargs):
    # delete friend(only available when the status of request is 'Accepted')
        user_1 = Author.objects.get(id=request.data["from_user"])
        user_2 = Author.objects.get(id=request.data["to_user"])
        if FriendRequest.objects.filter(from_user=user_1, to_user=user_2, status='A').exists():
        # user1 create the friend request and user1 delete 
            FriendRequest.objects.filter(from_user=user_1, to_user=user_2, status='A').delete()
            return Response("Successfully delete this friend!")
        elif FriendRequest.objects.filter(from_user=user_2, to_user=user_1, status='A').exists():
        # user2 create the friend request and userr1 delete
            FriendRequest.objects.filter(from_user=user_2, to_user=user_1, status='A').delete()
            return Response("Successfully delete this friend!")
        else:
            return Response("Unable to delete because you are not friends.")

    
