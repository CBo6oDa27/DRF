from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson

NULLABLE = {"blank": True, "null": True}


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите адрес элестронной почты"
    )
    phone = models.CharField(
        max_length=35, verbose_name="Телефон", help_text="Укажите телефон", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        **NULLABLE
    )
    city = models.CharField(
        max_length=35, verbose_name="Город", help_text="Укажите город", **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):

    PAYMENT_METHODS = (("Cash", "Наличные"), ("Transfer on account", "Перевод на счет"))

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Оплаченный курс", **NULLABLE
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Оплаченный урок", **NULLABLE
    )
    amount = models.BigIntegerField(verbose_name="Сумма оплаты")
    method = models.CharField(
        max_length=27,
        default="Cash",
        choices=PAYMENT_METHODS,
        verbose_name="Способ оплаты",
    )

    session_id = models.CharField(max_length=255, verbose_name="Id сессии", **NULLABLE)
    payment_link = models.URLField(
        max_length=400, verbose_name="Ссылка на оплату", **NULLABLE
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscription",
        verbose_name="пользователь",
        **NULLABLE
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="курс", **NULLABLE
    )

    def __str__(self):
        return f'{self.user}, {self.course}'

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
