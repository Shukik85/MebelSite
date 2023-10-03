from django.db import models
from clients.models import Clients


class Home(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Версия", null=False, unique=True
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    is_active = models.BooleanField(verbose_name="Активный", default=False)

    offer = models.ManyToManyField(
        "Card",
        verbose_name="Главное предложение",
        related_name="offer",
        limit_choices_to={"category": "offer"},
        blank=False,
    )

    info = models.ManyToManyField(
        "Card",
        verbose_name="О нас",
        related_name="info",
        limit_choices_to={"category": "info"},
        blank=False,
    )

    advantage = models.ManyToManyField(
        "Card",
        verbose_name="Из чего наша продукция",
        related_name="advantage",
        limit_choices_to={"category": "advantage"},
        blank=False,
    )

    works = models.ManyToManyField(
        "Card",
        verbose_name="Наши работы",
        related_name="works",
        limit_choices_to={"category": "works"},
        blank=False,
    )

    made = models.ManyToManyField(
        "Card",
        verbose_name="Этапы выполнения заказа",
        related_name="made",
        limit_choices_to={"category": "made"},
        blank=False,
    )

    partnership = models.ManyToManyField(
        "Card",
        verbose_name="Как происходит сотрудничество",
        related_name="partnership",
        limit_choices_to={"category": "partnership"},
        blank=False,
    )

    accordeon = models.ManyToManyField(
        "Card",
        verbose_name="Частые вопросы",
        related_name="accordeon",
        limit_choices_to={"category": "accordeon"},
        blank=False,
    )

    form = models.ForeignKey(
        to=Clients,
        verbose_name="Форма обратной связи",
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"
        ordering = ["-created_at"]


CATEGORI = [
    ("offer", "Главное Предложение"),
    ("info", "О нас"),
    ("advantage", "Преимущество нашей продукции"),
    ("works", "Наши работы"),
    ("made", "Этапы производства"),
    ("partnership", "Сотрудничество"),
    ("accordeon", "Вопросы"),
]


class Card(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    category = models.CharField(
        choices=CATEGORI, blank=False, null=True, verbose_name="Категория"
    )
    version = models.CharField(
        max_length=3, blank=False, null=True, verbose_name="Версия"
    )
    title = models.CharField(
        max_length=150, blank=True, null=True, verbose_name="Заголовок"
    )
    img = models.ImageField(
        upload_to="media/%Y/%m/%d", blank=True, null=True, verbose_name="Изображение"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Текст")

    def __str__(self):
        return f"{self.version}"

    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"
        ordering = [
            "-created_at",
        ]


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
