from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
import uuid

class Author(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, default="password")
    display_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)


options = (('draft','Draft'),
    ('published','Published')
)


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status= 'published')

    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256, default="")
    authorId = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    published = models.DateTimeField(default=timezone.now)
    
    # image = models.ImageField(null = True, blank = True, upload_to= "images/")
    status = models.CharField(max_length = 10, choices = options, default = 'published')

    objects= models.Manager()#defaut
    postobjects = PostObjects()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=256, default="")
    authorId = models.ForeignKey(Author, on_delete=models.CASCADE)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    published = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes", null=True, blank=True)
    commentId = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes", null=True, blank=True)
    published = models.DateTimeField(default=timezone.now)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(Author, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Author, related_name='to_user', on_delete=models.CASCADE)
