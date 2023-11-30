from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rank = models.IntegerField(default=0)

    def update_rating(self):
        pass

class Category(models.Model):
    name = models.CharField(unique=True)


class Post(models.Model):
    news = 'NEWS'
    article = 'ARTCL'

    TYPES = [
        (news, 'Новость'),
        (article, 'Статья')
    ]
    post_type = models.CharField(max_length=5, choices=TYPES, default=news)
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(default='***')
    text = models.TextField()
    post_rank = models.IntegerField(default=0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.post_rank += 1
        self.save()

    def dislike(self):
        self.post_rank -= 1
        self.save()

    def preview(self):
        return f'{self.text[:124]}...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    comment_rank = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self.comment_rank += 1
        self.save()

    def dislike(self):
        self.comment_rank -= 1
        self.save()
