# Generated by Django 4.2.5 on 2023-10-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_alter_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(default='Гость', editable=False, verbose_name='Отправитель'),
        ),
    ]
