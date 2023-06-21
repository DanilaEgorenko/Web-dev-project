from django.contrib import admin
from .models import Message, Chat

class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'text', 'chat']

class ChatAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat, ChatAdmin)