# Generated by Django 5.1 on 2024-08-13 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1, verbose_name='Позиция сайта в рейтинге')),
                ('logo_url', models.URLField(verbose_name='URL логотипа файла')),
                ('name', models.CharField(max_length=64, verbose_name='Название сайта')),
                ('rating', models.CharField(default='★★★★★', max_length=8, verbose_name='Рейтинг сайта')),
                ('reviews', models.IntegerField(default=213, verbose_name='Кол-во отзывов')),
                ('description', models.TextField(verbose_name='Описание сайта')),
                ('url', models.URLField(verbose_name='URL адрес сайта')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.TextField(default='Сообщение главного меню', verbose_name='Текст меню')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.CharField(max_length=32, verbose_name='Id чата пользователя')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Является ли пользователь админом')),
                ('action', models.CharField(default='', max_length=128, verbose_name='Действие пользователя')),
            ],
        ),
    ]
