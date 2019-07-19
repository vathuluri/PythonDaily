from django.conf import settings
from django.core.mail import send_mail
from django.template import Engine, Context

from myproject.celery import app


def render_template(template, context):
    engine = Engine.get_default()

    tmpl = engine.get_template(template)

    return tmpl.render(Context(context))
    
@celery_app.task(bind=True, default_retry_delay=10 * 60)
def send_mail_task(self, recipients, subject, template, context):
    message = render_template(f'{template}.txt', context)
    html_message = render_template(f'{template}.html', context)
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipients,
            fail_silently=False,
            html_message=html_message
        )
    except smtplib.SMTPException as ex:
        self.retry(exc=ex)

send_mail_task.delay(('noreply@example.com', ), 'Celery cookbook test', 'test', {})