from django.conf import settings
from django.core.mail import send_mail
from django.template import Engine, Context

from myproject.celery import app


def render_template(template, context):
    engine = Engine.get_default()

    tmpl = engine.get_template(template)

    return tmpl.render(Context(context))
    

@app.task
def send_mail_task(recipients, subject, template, context):
    send_mail(
        subject=subject,
        message=render_template(f'{template}.txt', context),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
        fail_silently=False,
        html_message=render_template(f'{template}.html', context)
    )

send_mail_task.delay(('noreply@example.com', ), 'Celery cookbook test', 'test', {})