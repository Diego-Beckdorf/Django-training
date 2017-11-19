from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')


class Comment(models.Model):
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_by = models.OneToOneField(User, on_delete=models.CASCADE)


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    liked_by = models.OneToOneField(User, on_delete=models.CASCADE)
