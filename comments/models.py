from django.db import models
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)