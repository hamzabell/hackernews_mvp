from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    upvotes_count = models.IntegerField(default=0)
    author_name = models.CharField(max_length=255)