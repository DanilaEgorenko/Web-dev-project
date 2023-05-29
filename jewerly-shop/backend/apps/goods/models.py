"""
Модуль с моделью товаров
"""

from django.db import models


class Good(models.Model):
    """Модель товара"""
    name = models.CharField(verbose_name="Название", max_length=64)
    price = models.DecimalField(verbose_name="Цена", max_digits=9, decimal_places=2, default=0.00)
    category = None
    alloy = models.CharField(verbose_name="Сплав", max_length=64, default="copper")

    class Meta:
        verbose_name = "Good"
        verbose_name_plural = "Goods"

    def __str__(self):
        return str(self.name)
