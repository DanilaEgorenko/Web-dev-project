from django.contrib import admin
from .models import Promocode


class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'users',
                    'count_of_uses_user',
                    'count_of_uses',
                    'name',
                    'deadline')
    list_display_links = ('id',
                    'users',
                    'count_of_uses_user',
                    'count_of_uses',
                    'name',
                    'deadline')


admin.site.register(Promocode, PromocodeAdmin)
