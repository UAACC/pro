from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
#from django.contrib.auth import password_validation
# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True, editable=False)
    
    #host = models.URLField(default=DEFAULT_HOST)
    displayName = models.CharField(max_length=150)
    github = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_approve = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]