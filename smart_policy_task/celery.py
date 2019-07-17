import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smart_policy_task.settings")

app = Celery("smart_policy_task")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-report-every-single-minute": {
        "task": "main_app.tasks.update_videos_list",
        "schedule": crontab(minute="*/10"),
    }
}
