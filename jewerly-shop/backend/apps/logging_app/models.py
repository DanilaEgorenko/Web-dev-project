from django.db import models

class VisitLog(models.Model):
    timestamp = models.DateTimeField(verbose_name="Время", auto_now_add=True)
    url = models.CharField(verbose_name="URL", max_length=200)
    method = models.CharField(verbose_name="Метод", max_length=10)
    user_agent = models.CharField(verbose_name="Пользователь", max_length=200)

    class Meta:
        verbose_name = "VisitLog"
        verbose_name_plural = "VisitLogs"

    def __str__(self):
        return str(self.timestamp)