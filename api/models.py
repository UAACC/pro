from django.db import models
from django.contrib.postgres.fields import ArrayField
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
    friend_requests = ArrayField(models.TextField())
    posts = ArrayField(models.TextField())


options = (('draft','Draft'),
    ('published','Published')
)


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status= 'published')

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    authorId = models.TextField()
    published = models.DateTimeField(auto_now_add=True, null=True)
    tags = ArrayField(models.TextField())
    comments = ArrayField(models.TextField())
    likes = ArrayField(models.TextField())
    # image = models.ImageField(null = True, blank = True, upload_to= "images/")
    status = models.CharField(max_length = 10, choices = options, default = 'published')
    # objects= models.Manager()
    # postobjects = PostObjects()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    authorId = models.TextField()
    likes = ArrayField(models.TextField())
    published = models.DateTimeField(auto_now_add=True)


class FriendRequest(models.Model):
    from_user = models.TextField()
    to_user = models.TextField()