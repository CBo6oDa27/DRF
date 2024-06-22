from config import settings
from materials.models import Course
from users.models import Subscription, User
from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime, timezone , timedelta


@shared_task
def notificator_subscription_update(course_id):
    """ Рассылка уведомлений об обновлении курса"""
    course = Course.objects.get(pk=course_id)
    subscribers = Subscription.objects.get(course=course_id)

    send_mail(
        subject=f'Обновление вашего курса {course.name}',
        message=f'Курс {course.description},на который вы подписаны обновлён',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscribers.user.email]
    )


@shared_task
def deactivate_old_user():
    """Отключение пользователей, не входивших на сайт более 30 дней"""
    active_users = User.objects.filter(is_active=True)
    now = datetime.now(timezone.utc)
    for user in active_users:
        if user.last_login:
            if now - user.last_login > timedelta(days=1):
                user.is_active = False
                user.save()

