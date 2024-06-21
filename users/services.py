import stripe
from forex_python.converter import CurrencyRates

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
