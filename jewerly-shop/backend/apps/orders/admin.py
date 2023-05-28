from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'user_id')
    list_display_links = ('id',
                          'user_id')


admin.site.register(Order, OrderAdmin)
