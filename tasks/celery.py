import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

app = Celery('blog')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'delete-likes-1-minutes': {
        'task': 'tasks.tasks.main.reset_likes',
        'schedule': crontab(),
    }
}


# celery -A tasks beat -l debug --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A tasks worker -l info
app.autodiscover_tasks()