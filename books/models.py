from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify

 
class Category(models.Model):
    name = models.CharField(max_length=50, default=None, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Category name={self.name}>"
    
    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        super().save(*args, **kwargs)


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username
        

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    url = models.URLField(max_length=255)
    description = models.TextField(max_length=800, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='books')
    favorite = models.ManyToManyField('User', related_name='favorited_by_user')
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Book title={self.title}>"

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)