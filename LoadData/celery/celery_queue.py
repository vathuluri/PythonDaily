CELERY_TASK_ROUTES = {
    'myproject.apps.mail.tasks.send_mail_task': {'queue': 'mail', },
}


#Python Celery Long Running Tasks
@celery_app.task
def send_good_morning_mail_task(offset=0, limit=100):
    users = User.objects.filter(is_active=True).order_by('id')[offset:offset + limit]
    for user in users:
        send_good_morning_mail(user)

    if len(users) >= limit:
        send_good_morning_mail_task.delay(offset + limit, limit)