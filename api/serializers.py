from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Author, Post, Comment, Like

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


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ['id', 'postId', 'commentId', 'published']


class CommentSerializer(serializers.ModelSerializer):

    likes = LikeSerializer(many=True, required=False)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'authorId', 'postId', 'likes', 'published']


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, required=False)
    likes = LikeSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'authorId', 'comments', 'likes', 'published','image','status']

    

class UpdateSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'published','image','status']




# class FriendRequestSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = FriendRequest
#         fields = ('id', 'to_user', 'from_user')


class AuthorSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, required=False)
    # out_requests = FriendRequestSerializer(many=True)
    # in_requests = FriendRequestSerializer(many=True)

    class Meta:
        model = Author
        # fields = ('id', 'username', 'display_name', 'email', 'bio', 'github', 'is_approved', 'posts', 'out_requests', 'in_requests')
        fields = ('id', 'username', 'display_name', 'email', 'bio', 'github', 'is_approved', 'posts')


