from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

#
# class User(AbstractUser):
#     friends = models.ManyToManyField("User", blank=True)

class Author(models.Model):
    username = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_approved = models.BooleanField(default=False)

class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="posts")
    published = models.DateTimeField(default=timezone.now)

#
# class Friend_Request(models.Model):
#     from_user = models.ForeignKey(
#         User, related_name='from_user', on_delete=models.CASCADE
#     )
#     to_user = models.ForeignKey(
#         User, related_name='to_user', on_delete=models.CASCADE
#     )