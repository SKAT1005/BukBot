import random

from django.db import models


class Site(models.Model):
    number = models.IntegerField(default=1, verbose_name='Позиция сайта в рейтинге')
    logo_url = models.URLField(verbose_name='URL логотипа файла')
    name = models.CharField(max_length=64, verbose_name='Название сайта')
    rating = models.CharField(max_length=8, default='★' * 5, verbose_name='Рейтинг сайта')
    reviews = models.IntegerField(default=random.randint(200, 1000), verbose_name='Кол-во отзывов')
    description = models.TextField(verbose_name='Описание сайта')
    url = models.URLField(verbose_name='URL адрес сайта')


class User(models.Model):
    chat_id = models.CharField(max_length=32, verbose_name='Id чата пользователя')
    is_admin = models.BooleanField(default=False, verbose_name='Является ли пользователь админом')
    action = models.CharField(max_length=128, default='', verbose_name='Действие пользователя')


class Text(models.Model):
    menu = models.TextField(default='Сообщение главного меню', verbose_name='Текст меню')
