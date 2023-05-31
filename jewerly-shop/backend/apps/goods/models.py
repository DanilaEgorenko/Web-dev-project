"""
Модуль с моделью товаров
"""

from django.db import models


class Good(models.Model):
    """Модель товара"""
    title = models.CharField(verbose_name="Название", max_length=64)
    price = models.DecimalField(verbose_name="Цена", max_digits=9, decimal_places=2, default=0.00)
    material = models.CharField(verbose_name="Материал", max_length=32, default="Silver")
    img = models.ImageField(verbose_name="Изоюражение", max_length=9999, default=None, null=True, upload_to ='static/img/')
    color = models.CharField(verbose_name="Цвет", max_length=32, default="Серый")
    category = None

    class Meta:
        verbose_name = "Good"
        verbose_name_plural = "Goods"

    def __str__(self):
        return str(self.title)
