from celery import shared_task
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from post.models import Blog
UserModel = get_user_model()

@shared_task
def reset_likes():
    print('ISLEYIRRR111111')
    ids = []
    blogs = Blog.objects.values()
    for i in range(blogs.count()):
        ids.append(blogs[i]['id'])

    for id in ids:
        post = get_object_or_404(Blog, id=id)
        user_liked = post.likes.values('id')
        for user in user_liked:
            post.likes.remove(user['id'])



# celery -A tasks.celery.app worker -l debug
# celery -A tasks.celery.app beat -l debug

# celery -A tasks.celery.app beat -l debug --scheduler django_celery_beat.schedulers:DatabaseScheduler

#pip install -U django-celery-beat
