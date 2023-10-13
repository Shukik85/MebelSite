from django.db import models


class Contacts(models.Model):
    is_active = models.BooleanField(verbose_name="Активный", default=False)
    name = models.CharField(max_length=25, verbose_name="Имя", unique=True)
    adress = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=25, verbose_name="Телефон")
    mail = models.EmailField(verbose_name="Эл.почта")
    url = models.URLField(blank=True, default="https://", verbose_name="Ссылка URL:")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
        ordering = [
            "name",
        ]
