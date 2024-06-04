from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Введите описание курса", **NULLABLE
    )
    preview = models.ImageField(
        upload_to="materials/previews",
        verbose_name="Превью (картинка)",
        help_text="Загрузите превью",
        **NULLABLE
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Владелец"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание урока", help_text="Введите описание урока", **NULLABLE
    )
    preview = models.ImageField(
        upload_to="materials/previews",
        verbose_name="Превью (картинка)",
        help_text="Загрузите превью",
        **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Выберите курс урока",
        **NULLABLE
    )
    video_url = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео урока",
        **NULLABLE
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        **NULLABLE,
        verbose_name="Владелец"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
