# Generated by Django 5.0.6 on 2024-06-21 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="payment_link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Id сессии"
            ),
        ),
    ]
