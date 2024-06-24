import stripe
from forex_python.converter import CurrencyRates
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json
from datetime import datetime, timedelta

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def convert_rub_to_dollars(amount):
    """Конвертация рублей в доллары"""
    cur_rates = CurrencyRates()
    rate = cur_rates.get_rate("RUB", "USD")
    return int(amount * rate)


def create_stripe_product(instance):
    """Создаем продукт в stripe"""

    title_product = f"{instance.course.name}"
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


def create_stripe_price(amount, stripe_product_id):
    """Создаем цену в stripe"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product=stripe_product_id,
    )


def create_stripe_session(price):
    """Создаем сессию на оплату в stripe"""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")


def set_schedule(*args, **kwargs):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=24,
        period=IntervalSchedule.DAYS,
    )

    PeriodicTask.objects.create(
        interval=schedule,  # we created this above.
        name='Deactivate users',  # simply describes this periodic task.
        task='DRF.tasks.deactivate_old_user',  # name of task.
        args=json.dumps(['']),
        kwargs=json.dumps({
            'be_careful': True,
        }),
        expires=datetime.utcnow() + timedelta(seconds=30)
    )

