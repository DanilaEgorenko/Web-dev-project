"""
Модуль менеджера для модели пользователя
"""
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    """
    Кастомный класс менеджера для пользователя,
    унаследовавший все, что встроино в стандартный
    менеджера для стандартного пользователя
    """

    def create_user(self, username, email, password=None):
        """ Создает и возвращает пользователя с почтой, паролем и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user