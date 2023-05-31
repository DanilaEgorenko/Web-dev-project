from django.contrib import admin
from .models import Good


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    list_display_links = ('title', 'price')


admin.site.register(Good, GoodsAdmin)
