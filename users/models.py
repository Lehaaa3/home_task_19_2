from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='страна')
    email_verification = models.CharField(max_length=35, verbose_name='код верификации email', **NULLABLE)
    email_is_active = models.BooleanField(default=False, verbose_name='активация почты')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
