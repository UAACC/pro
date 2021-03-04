from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Author, Post, Comment, Like, FriendRequest
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        author = Author.objects.create(username=user.username)
        return user


class CommentSerializer(serializers.ModelSerializer):

    likes = LikeSerializer(many=True, required=False)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'published']


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, required=False)
    likes = LikeSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'comments', 'likes', 'published','image','status']

    
class PostCreateSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, required=False)
    likes = LikeSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'authorId', 'comments', 'likes', 'published','image','status']


class UpdateSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'published','image','status']




class FriendRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendRequest
        fields = ('id', 'to_user', 'from_user')


class AuthorSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, required=False)
    friend_requests = FriendRequestSerializer(many=True, required=False)

    class Meta:
        model = Author
        fields = ('id', 'username', 'password', 'display_name', 'email', 'bio', 'github', 'is_approved', 'posts', 'friend_requests')
