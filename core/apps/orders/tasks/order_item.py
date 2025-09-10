import requests
from celery import shared_task

from core.apps.orders.models import OrderItem, Order
from config.env import env

token = env.str("BOT_TOKEN")

@shared_task
def send_orders_to_tg_bot(chat_id, product_name, quantity, username):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    message = (
        f"✅ Товар: {product_name}\n"
        f"🛒 Кол-во: {quantity}\n\n"

        f"Имя: {username}"
    )
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()


@shared_task
def send_message_order_user(chat_id, order_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    order = Order.objects.get(id=order_id)
    result = []
    for order_item in order.items.all():
        product_name = order_item.product.name
        unit = order_item.product.unity.name
        quantity = order_item.quantity
        price = order_item.price

        result.append(f"🔹 {product_name} {unit} ({quantity} x {price:.2f})")

    message = (
        f'⚡️ Оформлен новый заказ\n\n'

        f"Сумма заказа №{order.order_number}: {order.total_price}\n\n"
        
        f"{result}"
    )

    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response.json()
