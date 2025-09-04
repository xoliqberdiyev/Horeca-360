import requests
from celery import shared_task

from core.apps.orders.models import OrderItem
from config.env import env

token = env.str("BOT_TOKEN")

@shared_task
def send_orders_to_tg_bot(chat_id, product_name, quantity, price):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    message = (
        f"Mahsulot nomi: {product_name}\n"
        f"Mahsulot soni: {quantity}\n"
        f"Summa: {price}"   
    )
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

