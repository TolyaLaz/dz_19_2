from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    avatar = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name='Аватар', help_text='Загрузите аватар')
    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True, help_text='Введите номер телефона')
    country = models.CharField(max_length=50, verbose_name='Страна', blank=True, null=True, help_text='Введите страну')
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Введите адрес электронной почты')

    token = models.CharField(max_length=100, blank=True, null=True, verbose_name='Token')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

