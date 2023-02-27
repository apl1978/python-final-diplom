from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from orders.celery import app

from backend.models import ConfirmEmailToken, User

@app.task()
def new_user_registered(user_email, token_key, **kwargs):
    """
    отправляем письмо с подтрердждением почты
    """
    # send an e-mail to the user
    msg = EmailMultiAlternatives(
        # title:
        f"Password Reset Token for {user_email}",
        # message:
        token_key,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user_email]
    )
    msg.send()

@app.task()
def new_order(user_id, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    # send an e-mail to the user
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        # title:
        f"Обновление статуса заказа",
        # message:
        'Заказ сформирован',
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [user.email]
    )
    msg.send()
