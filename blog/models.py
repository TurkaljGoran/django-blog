from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('post title', max_length=255)
    content = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, made by {self.author}"

    def get_absolute_url(self):

        return reverse('blog:detail', kwargs={'pk': self.pk})