# Generated by Django 4.2.5 on 2023-10-15 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoryes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PhotoWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, null=True, unique=True, verbose_name='Объект')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('photo1', models.ImageField(max_length=255, upload_to='works/%Y/%m/%d', verbose_name='Фото1')),
                ('photo2', models.ImageField(max_length=255, upload_to='works/%Y/%m/%d', verbose_name='Фото2')),
                ('photo3', models.ImageField(max_length=255, upload_to='works/%Y/%m/%d', verbose_name='Фото3')),
                ('photo4', models.ImageField(blank=True, max_length=255, upload_to='works/%Y/%m/%d', verbose_name='Фото4')),
                ('photo5', models.ImageField(blank=True, max_length=255, upload_to='works/%Y/%m/%d', verbose_name='Фото5')),
                ('photo6', models.ImageField(blank=True, max_length=255, upload_to='works/%Y/%m/%d', verbose_name='Фото6')),
            ],
            options={
                'verbose_name': 'Фото работы',
                'verbose_name_plural': 'Фото работы',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Объект')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('description', models.TextField(blank=True, unique=True, verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='works.categoryes', verbose_name='Категории')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.clients', verbose_name='Заказчик')),
                ('photos', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='works.photoworks', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Выполненые работы',
                'verbose_name_plural': 'Выполненые работы',
                'ordering': ['-created_at', 'category'],
            },
        ),
    ]
