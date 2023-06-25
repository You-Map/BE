from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Purpose(models.Model):
    name = models.CharField(max_length=10)

class Location(models.Model):
    name = models.CharField(max_length=10)
    floor = models.IntegerField(default=0)

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='post/')
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE)
    purpose = models.ForeignKey(to=Purpose, on_delete=models.CASCADE)
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    likes = models.IntegerField(default=0)

class Comment(models.Model):
    writer=models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='내용', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='작성일')
    post = models.ForeignKey(to = 'Post', on_delete=models.CASCADE)