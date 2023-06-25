from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField()
    file = models.ImageField(upload_to='post_attachments/')
    likes = models.IntegerField()

