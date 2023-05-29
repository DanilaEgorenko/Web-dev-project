from django.contrib import admin
from .models import Good


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'alloy')
    list_display_links = ('name', 'price')


admin.site.register(Good, GoodsAdmin)
