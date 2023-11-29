from django.db import models
from datetime import datetime, timezone


class Author(models.Model):
    user_rank = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField(unique=True)


class Post(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(default='***')
    text = models.TextField()
    post_rank = models.IntegerField(default=0)


class PostCategory(models.Model):
    pass


class Comment(models.Model):
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    comment_rank = models.IntegerField(default=0)

