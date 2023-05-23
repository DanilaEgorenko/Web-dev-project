"""
Модуль с моделью заказов
"""

from django.db import models

class Order(models.Model):
    """Модель заказа"""

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")
        
        
    def __str__(self):
        return str(self.pk)
