from django.contrib import admin
from .models import Article


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'create_date', 'change_date']
    list_display_links = ['title']


admin.site.register(Article, ArticlesAdmin)
