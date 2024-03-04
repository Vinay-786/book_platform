from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    likes = models.IntegerField(null=True)
    image = models.ImageField(default='default.jpg', upload_to='book_images')

    def __str__(self):
          return f"{self.title}"

class Comments(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', null=True)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
          return f"{self.content}"
