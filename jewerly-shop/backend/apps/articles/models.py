"""
Модуль с моделью статей
"""

from django.db import models

class Article(models.Model):
    """Модель статьи"""
    title = models.CharField(verbose_name="Название", max_length=60)
    description = models.TextField(verbose_name="Текст")
    create_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    change_date = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return str(self.title)
 