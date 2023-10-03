from django.db import models

class Clients(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    name = models.CharField(max_length=50, verbose_name='Имя заказчика', blank=False, null=True)
    adress = models.CharField(max_length=50, verbose_name='Адрес заказчика', blank=False, null=True, unique=True)
    phone = models.CharField(max_length=50, verbose_name='Телефон заказчика', blank=False, null=True)
    mail = models.EmailField(max_length=50, verbose_name='Эл.почта заказчика', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created_at',] 
