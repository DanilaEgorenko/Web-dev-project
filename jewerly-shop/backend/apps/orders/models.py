"""
Модуль с моделью заказов
"""

from django.db import models

from apps.users.models import User
from apps.goods.models import Good


class Order(models.Model):
    """Модель заказа"""
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name="Индификатор пользователя")
    goods_list = models.ManyToManyField(Good)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    def __str__(self):
        return str(self.pk)
