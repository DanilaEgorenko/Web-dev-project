"""
Модуль с моделью товаров
"""

from django.db import models

class Good(models.Model):
    """Модель товара"""
    name = models.CharField(verbose_name="Название", max_length=64)
    

    class Meta:
        verbose_name = ("Good")
        verbose_name_plural = ("Goods")

    def __str__(self):
        return str(self.name)
