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

        return token

    def send_mail(self, subject, message):
        """
        Отправляет письмо с переданной темой и текстом
        """
        send_mail(subject, message, from_email="1@mail.ru", recipient_list=["2@mail.ru"])


class GoogleAuthTokens(models.Model):
    access_token = models.CharField(verbose_name='Access token' ,max_length=1500)
    id_token = models.CharField(verbose_name='Id token', max_length=500)
    expires_in = models.IntegerField(verbose_name='Expires in')
    created_at = models.DateTimeField(verbose_name='Creation date', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name = 'OAuth токен'
        verbose_name_plural = 'OAuth токены'
