import requests
from celery import shared_task

from core.apps.orders.models import OrderItem
from config.env import env

token = env.str("BOT_TOKEN")

@shared_task
def send_orders_to_tg_bot(
    chat_id, product_name, quantity, price, payment_type, 
    delivery_type, contact_number, address, comment, name
):
    if payment_type == 'CASH':
        payment_type = "Naqd to'lov"
    elif payment_type == 'CARD':
        payment_type = "Karta orqali to'lov"
    elif payment_type == 'ACCOUNT_NUMBER':
        payment_type = "Hisob raqam orqali to'lov"
        
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    message = (
        f"📦 Mahsulot nomi: {product_name}\n"
        f"🔢 Mahsulot soni: {quantity}\n"
        f"💰 Summa: {price}\n\n"

        f"📞 Aloqa uchun: (99) 099-91-92"
    )
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()

