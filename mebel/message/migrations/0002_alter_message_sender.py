# Generated by Django 4.2.5 on 2023-10-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(editable=False, verbose_name='Отправитель'),
        ),
    ]