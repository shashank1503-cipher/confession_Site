from django.db import models

# Create your models here.
class Post(models.Model):
    postContent = models.TextField()
    user = models.CharField(max_length=100)
class Likes(models.Model):
    post_id = models.IntegerField()
    user = models.CharField(max_length=100)
