from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Author, Post

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

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'published']

class AuthorSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True)

    class Meta:
        model = Author
        fields = ('id', 'token', 'username', 'display_name', 'email', 'password', 'bio', 'github', 'is_approved', 'posts')



