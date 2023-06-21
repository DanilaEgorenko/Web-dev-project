from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import VisitLog

@receiver(post_save, sender=VisitLog)
def cache_visit_log(sender, instance, **kwargs):
    # Кешируем лог в виде строки
    log_string = f"{instance.timestamp} - {instance.method} {instance.url}\n"
    cache.add('visit_logs', log_string)

    # Здесь вы можете определить логику для периодической записи в базу данных
    # Например, каждые 100 записей или каждые 5 минут можно вызывать функцию, 
    # которая будет переносить кешированные логи в базу данных.
