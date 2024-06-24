from config import settings
from materials.models import Course
from users.models import Subscription, User
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def notificator_subscription_update(course_id):
    """ Рассылка уведомлений об обновлении курса"""
    course = Course.objects.get(pk=course_id)
    subscribers = Subscription.objects.filter(course=course_id)
    sub_email_list = []
    for subscriber in subscribers:
        sub_email_list.append(subscriber.user.email)
    send_mail(
        subject=f'Обновление вашего курса {course.name}',
        message=f'Курс {course.description},на который вы подписаны обновлён',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=sub_email_list
    )


