from django.shortcuts import render
from rest_framework import viewsets
from. models import Post
from .serializers import PostSerializer
from rest_framework.authentication import TokenAuthentication

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication, )