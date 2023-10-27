from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):

    sender = models.ForeignKey(
        User,
        verbose_name="Отправитель",
        to_field="username",
        related_name="sender",
        on_delete=models.CASCADE,
        editable=False,
    )
    theme = models.CharField(verbose_name="Тема")
    msg = models.TextField(verbose_name="Сообщение")
    recipient = models.ForeignKey(
        User,
        verbose_name="Получатель",
        to_field="username",
        related_name="recipient",
        on_delete=models.CASCADE,
    )
