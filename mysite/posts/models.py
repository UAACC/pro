from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256, default="")
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(default=timezone.now)