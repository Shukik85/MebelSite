from django.db import models
from django.urls import reverse_lazy
from clients.models import Clients


class PhotoWorks(models.Model):
    name = models.CharField(
        max_length=25, verbose_name="Объект", blank=False, unique=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    photo1 = models.ImageField(
        max_length=255, upload_to="works/%Y/%m/%d", blank=False, verbose_name="Фото1"
    )
    photo2 = models.ImageField(
        max_length=255, upload_to="works/%Y/%m/%d", blank=False, verbose_name="Фото2"
    )
    photo3 = models.ImageField(
        max_length=255, upload_to="works/%Y/%m/%d", blank=False, verbose_name="Фото3"
    )
    photo4 = models.ImageField(
        max_length=255, upload_to="works/%Y/%m/%d", blank=True, verbose_name="Фото4"
    )
    photo5 = models.ImageField(
        max_length=255, upload_to="works/%Y/%m/%d", blank=True, verbose_name="Фото5"
    )
    photo6 = models.ImageField(
        max_length=255, upload_to="works/%Y/%m/%d", blank=True, verbose_name="Фото6"
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Фото работы"
        verbose_name_plural = "Фото работы"
        ordering = ["-created_at"]


class Categoryes(models.Model):
    name = models.CharField(max_length=25, verbose_name="Название", unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse_lazy("by_category", kwargs={"pk": self.pk})


class Works(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Объект", blank=False, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    client = models.ForeignKey(
        to=Clients,
        verbose_name="Заказчик",
        blank=False,
        null=True,
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        to=Categoryes,
        verbose_name="Категории",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    description = models.TextField(blank=True, verbose_name="Описание", unique=True)
    photos = models.OneToOneField(
        to=PhotoWorks,
        verbose_name="Фото",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def get_photo(self):
        if self.photos:
            obj = self.photos
            set_photo = []
            try:
                for i in range(1, 7):
                    src = []
                    exec(f"src.append(obj.photo{i}.url)", {"obj": obj, "src": src})
                    set_photo += src
            except ValueError:
                pass
            return set_photo
        else:
            return "Фото нет"

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse_lazy("work_view", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Выполненые работы"
        verbose_name_plural = "Выполненые работы"
        ordering = ["-created_at", "category"]
