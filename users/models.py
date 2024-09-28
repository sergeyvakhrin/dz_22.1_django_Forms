from django.contrib.auth.models import AbstractUser
from django.db import models

from blog.models import NULLABLE


class User(AbstractUser):
    """ Класс для модели пользователей """
    username = None
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="Укажите почту")
    avatar = models.ImageField(upload_to="users/", verbose_name="Фото", **NULLABLE, help_text="Загрузите фото")
    phone = models.CharField(max_length=35, verbose_name="Телефон", help_text="Введите номер телефона", **NULLABLE)
    country = models.CharField(max_length=50, verbose_name="Страна", help_text="Введите страну", **NULLABLE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
