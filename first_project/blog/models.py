from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # import user so we know who post the post (one to many relationship)
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # auto_now_add=True - to keep just first datetime
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # User table as related key here

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
