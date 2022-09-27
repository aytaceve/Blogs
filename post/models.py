from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


