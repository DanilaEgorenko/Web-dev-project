"""
Модуль с моделью промокода
"""

from django.db import models

from apps.users.models import User
from apps.promocodes.models import Promocode


class Promocode(models.Model):
    """Модель промокода"""
    id = models.AutoField(primary_key=True)
    users = models.ManyToManyField(default=None, 
                                   verbose_name="Пользователи")
    count_of_uses_user = models.IntegerField(default=None, 
                                             verbose_name="Количество использований от одного пользователя")
    count_of_uses = models.IntegerField(default=None, 
                                        verbose_name="Количество использований")
    name = models.CharField(default=None, 
                            verbose_name="Название промокода", max_length=12)
    deadline = models.DateField(default=None, 
                                verbose_name="Срок действия")

    class Meta:
        verbose_name = ("Промокод")
        verbose_name_plural = ("Промокоды")

    def __str__(self):
        return str(self.pk)
