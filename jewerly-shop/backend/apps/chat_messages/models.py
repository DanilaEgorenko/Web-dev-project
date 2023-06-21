from django.db import models
from apps.users.models import User
from time import timezone

class Chat(models.Model):
    user1 = models.ForeignKey(User, verbose_name="Пользователь1", null=False, on_delete=models.CASCADE, related_name='user_1')
    user2 = models.ForeignKey(User, verbose_name="Пользователь2", null=False, on_delete=models.CASCADE, related_name='user_2')

    class Meta:
        verbose_name = ("Чат")
        verbose_name_plural = ("Чаты")

    def __str__(self):
        return str(self.pk)
    

class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="chat", on_delete=models.CASCADE)
    text = models.CharField(max_length=256, verbose_name='Текст сообщения', null=False)
    user = models.ForeignKey(User, verbose_name="Отправитель", null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = ("Сообщение")
        verbose_name_plural = ("Сообщения")

    def __str__(self):
        return str(self.pk)