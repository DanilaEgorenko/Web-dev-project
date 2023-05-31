from django.db import models
from apps.users.models import User
from apps.goods.models import Good

# Create your models here.
class Reviews(models.Model):
    username = models.ForeignKey(User, db_index=True, max_length=255, on_delete=models.CASCADE, verbose_name='Автор отзыва')
    product = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name="Товар", max_length=64, related_name='reviews_good')
    text = models.TextField(max_length=250, verbose_name='Текст отзыва')
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'