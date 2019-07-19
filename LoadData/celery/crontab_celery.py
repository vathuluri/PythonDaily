from celery.schedules import crontab


CELERY_BEAT_SCHEDULE = {
    'monday-statistics-email': {
        'task': 'myproject.apps.statistics.tasks.monday_email',
        'schedule': crontab(day_of_week=1, hour=7),
    },
}


from datetime import datetime


send_mail_task.apply_async(
    (('noreply@example.com', ), 'Celery cookbook test', 'test', {}),
    countdown=15 * 60
)

send_mail_task.apply_async(
    (('noreply@example.com', ), 'Celery cookbook test', 'test', {}),
    eta=datetime(2019, 5, 20, 7, 0)