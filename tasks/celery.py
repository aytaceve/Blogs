import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

app = Celery('blog')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'delete-likes': {
        'task': 'tasks.tasks.main.reset_likes',
        'schedule': crontab(minute=0, hour=0),
        # 'schedule': crontab(minute=0, hour=0)
    }
}


app.autodiscover_tasks()