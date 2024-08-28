from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    avatar = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name='Аватар',
                               help_text='Загрузите аватар')
    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True,
                             help_text='Введите номер телефона')
    country = models.CharField(max_length=50, verbose_name='Страна', blank=True, null=True, help_text='Введите страну')
    email = models.EmailField(unique=True, verbose_name='Почта', help_text='Введите адрес электронной почты')

    token = models.CharField(max_length=100, blank=True, null=True, verbose_name='Token')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
