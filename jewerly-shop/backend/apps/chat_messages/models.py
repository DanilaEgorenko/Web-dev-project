from django.db import models
from apps.users.models import User

class Message(models.Model):
    chat_id = models.IntegerField(verbose_name="Id чата", null=False)
    text = models.CharField(verbose_name="Текст сообщения", null=False, max_length=256)
    user = models.ForeignKey(User, verbose_name="Пользователь", null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Сообщение")
        verbose_name_plural = ("Сообщения")

    def __str__(self):
        return str(self.pk)