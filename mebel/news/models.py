from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name="заголовок")
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        editable=False,  # Запретить изменения чтобы убрать из ручного редактирования
    )
    content = models.TextField(blank=True, verbose_name="текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="изменено")
    photo = models.ImageField(upload_to="media/%Y/%m/%d", verbose_name="фото")
    is_published = models.BooleanField(default=True, verbose_name="публикация")
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, null=True, verbose_name="Категория"
    )

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse_lazy("news:News", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Категория")

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse_lazy("news:Category", kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
