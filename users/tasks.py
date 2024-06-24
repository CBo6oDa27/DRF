from config import settings
from materials.models import Course
from users.models import Subscription, User
from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime, timezone , timedelta


@shared_task
def deactivate_old_user():
    """Отключение пользователей, не входивших на сайт более 30 дней"""
    active_users = User.objects.filter(is_active=True)
    now = datetime.now(timezone.utc)
    for user in active_users:
        if user.last_login:
            if now - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
