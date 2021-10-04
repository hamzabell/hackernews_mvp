from __future__ import absolute_import, unicode_literals

from celery import shared_task


from posts.models import Post

@shared_task
def reset_upvotes():
    all_posts = Post.objects.all()

    for post in all_posts:
        post.upvotes_count = 0
        post.save()