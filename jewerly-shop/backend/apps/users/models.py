"""
Модуль с моделью пользователя
"""
import jwt
from datetime import datetime, timedelta, timezone
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import UserManager
from django.core.mail import send_mail


class User(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя"""

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели """
        return self.email

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем
        простого вызова user.token
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Метод для генерации JWT токена
        """

        dt = datetime.now() + timedelta(days=1)
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp()),
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def send_mail(self, subject, message):
        """
        Отправляет письмо с переданной темой и текстом
        """
        send_mail(subject, message, from_email="1@mail.ru", recipient_list=["2@mail.ru"])
