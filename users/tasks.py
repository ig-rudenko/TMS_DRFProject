import time

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import User


@shared_task()
def daily_notifications_task():
    """
    Daily notifications task
    """

    users = User.objects.all().only("email", "is_active")

    for user in users:
        if not user.email or not user.is_active:
            continue

        print(f"Sending email to {user.email}")
        status = send_mail(
            "Daily notifications",
            "This is a daily notification",
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        print(status)
        time.sleep(1)
