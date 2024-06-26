# Generated by Django 5.0.6 on 2024-05-31 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0003_alter_lesson_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="video_url",
            field=models.URLField(
                blank=True,
                help_text="Укажите ссылку на видео урока",
                null=True,
                verbose_name="Ссылка на видео",
            ),
        ),
    ]
