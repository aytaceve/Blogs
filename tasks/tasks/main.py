from celery import shared_task
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from post.models import Blog
UserModel = get_user_model()

@shared_task
def reset_likes():
    print('STARTING TASK-------')
    # post = get_object_or_404(Blog, id=request.POST.get('post_id'))
    # posts = Blog.objects.values()
    # for post in posts:
    #     user_liked = post.likes.values('id')
    #     for user in user_liked:
    #         post.likes.remove(user['id'])
    print('FINISH TASK-------')

# celery -A tasks beat -l info
#
# celery -A tasks.celery.app beat -l debug

# celery -A tasks.celery.app worker -l debug --scheduler django_celery_beat.schedulers:DatabaseScheduler

#pip install -U django-celery-beat
