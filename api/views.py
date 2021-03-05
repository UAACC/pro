from rest_framework import viewsets, status,generics
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from .serializers import AuthorSerializer, PostSerializer, CommentSerializer, LikeSerializer,UpdateSerializer,PostCreateSerializer,CategorySerializer
from .models import Author, Post, Category, Like, Comment
from django.http import JsonResponse, HttpResponse
from .permissions import IsOwnerOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny, )

    def create(self, request):
        try:
            author = Author.objects.get(username=request.data['username'])
            token = Token.objects.get(user=author)
            response = {'id': author.id, 'username': author.username, 'email': author.email, 'password': author.password, 'token': token.key}
            return JsonResponse(response)
        except:
            author = Author.objects.create(
                username=request.data['username'],
                password=request.data['password'],
                email=request.data['email'],
            )
            token = Token.objects.create(user=author)
            response = {'id': author.id, 'email': author.email, 'username': author.username, 'password': author.password, 'token': token.key}
            return JsonResponse(response)

# Like & Comment
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Post.postobjects.all()
    serializer_class = LikeSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    def create(self, request):
        author = Author.objects.get(username=request.user)
        try:
            commentId = request.data['comment']
            comment = Comment.objects.get(id=commentId)
            try:
                like = Like.objects.get(author=author, comment=comment)
                like.delete()
                return HttpResponse('Good request, like is deleted')
            except:
                Like.objects.create(author=author, comment=comment)
                return HttpResponse('Good request, like is created')
        except:
            try:
                postId = request.data['post']
                post = Post.objects.get(id=postId)
                try:
                    like = Like.objects.get(author=author, post=post)
                    like.delete()
                    return HttpResponse('Good request, like is deleted')
                except:
                    Like.objects.create(author=author, post=post)
                    return HttpResponse('Good request, like is created')
            except:
                return HttpResponse('Bad request')



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Post.postobjects.all()
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

    def create(self, request):
        author = Author.objects.get(username=request.user)
        content = request.data['content']
        post = Post.objects.get(id=request.data['post'])
        Comment.objects.create(author=author, post=post, content=content)
        return HttpResponse('Good request, comment created!')

    def patch(self, request):
        author = Author.objects.get(username=request.user)
        content = request.data['content']
        post = Post.objects.get(id=request.data['post'])
        try:
            comment = Comment.objects.get(author=author, post=post)
            print("1", author, post, comment)
            comment.update(content=content)
            print("2")
            comment.save()
            print("3")
            return HttpResponse('Good request, comment updated!')
        except: 
            return HttpResponse('Bad request')

class PostList(generics.ListAPIView):
    
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        #import pdb; pdb.set_trace()
        public_posts = Post.postobjects.filter(publicity = True)
        return public_posts

class PostCreate(generics.CreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )
    
    def create(self, serializer):
        serializer.save(Author=self.request.user)

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = (AllowAny, )

class UpdatePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = UpdateSerializer
    
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class DeletePost(generics.DestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, )
    

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
