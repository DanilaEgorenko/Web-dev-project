from django.contrib import admin
from .models import VisitLog


class VisitLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'url', 'method', 'user_agent')
    list_display_links = ('timestamp', )


admin.site.register(VisitLog, VisitLogAdmin)
