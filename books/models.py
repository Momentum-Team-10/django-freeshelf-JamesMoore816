from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Book:
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=800, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)