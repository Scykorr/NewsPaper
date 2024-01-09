from django.core.cache import cache
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rank = models.IntegerField(default=0)

    def update_rating(self):
        post_rank = self.post_set.aggregate(post_ranking=Sum('post_rank'))
        sum_post_rank = 0
        sum_post_rank += post_rank.get('post_ranking')

        comment_rank = self.author.comment_set.aggregate(comment_ranking=Sum('comment_rank'))
        sum_comm_rank = 0
        sum_comm_rank += comment_rank.get('comment_ranking')

        self.user_rank = sum_post_rank * 3 + sum_comm_rank
        self.save()

    def __str__(self):
        return self.author.username


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    news = 'NEWS'
    article = 'ARTCL'

    TYPES = [
        ('NEWS', 'Новость'),
        ('ARTCL', 'Статья')
    ]
    post_type = models.CharField(max_length=5, choices=TYPES, default=news)
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default='***')
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

    def __str__(self):
        return f'{self.title.title()}: {self.text[:15]}...'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete(f'news-{self.pk}')


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


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
