from django.db import models
from django.urls import reverse_lazy


class Proposal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    name = models.CharField(
        max_length=50,
        verbose_name="Имя заказчика",
        blank=False,
        null=True,
        error_messages="Максимум 50 символов",
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Телефон заказчика",
        blank=False,
        null=True,
        error_messages="Максимум 15 символов",
    )
    mail = models.EmailField(
        max_length=50,
        verbose_name="Эл.почта заказчика",
        blank=True,
        null=True,
        error_messages="Не правильный формат e-mail",
    )
    message = models.TextField(
        max_length=1000,
        verbose_name="Сообщение",
        blank=False,
        null=True,
        error_messages="Максимум 1000 символов",
    )
    files = models.FileField(
        upload_to="media/%Y/%m/%d",
        max_length=1000,
        verbose_name="Файлы",
        blank=True,
        null=True,
        error_messages="Неправильный формат файла",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = [
            "-created_at",
        ]

    def get_absolute_url(self):
        return reverse_lazy("home:home")