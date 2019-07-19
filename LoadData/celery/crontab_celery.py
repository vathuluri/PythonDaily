from celery.schedules import crontab


CELERY_BEAT_SCHEDULE = {
    'monday-statistics-email': {
        'task': 'myproject.apps.statistics.tasks.monday_email',
        'schedule': crontab(day_of_week=1, hour=7),
    },
}