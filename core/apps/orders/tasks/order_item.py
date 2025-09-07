import requests
from celery import shared_task

from core.apps.orders.models import OrderItem
from config.env import env

token = env.str("BOT_TOKEN")

@shared_task
def send_orders_to_tg_bot(chat_id, product_name, quantity, first_name, last_name):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    message = (
        f"✅ Товар: {product_name}\n"
        f"🛒 Кол-во: {quantity}\n\n"

        f"Имя: {first_name} {last_name}"
    )
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

