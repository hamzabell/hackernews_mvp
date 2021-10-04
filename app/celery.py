from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab




# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app',include=['app.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    "Reset up votes 11pm everyday": {
        "task": "app.tasks.reset_upvotes",  
        "schedule": crontab(hour='23',
                            minute=0,
                            )
    }
}

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()

