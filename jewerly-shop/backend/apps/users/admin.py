from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'username',
                    'email',
                    'is_active',
                    'is_staff',
                    'created_at',
                    'updated_at')
    list_display_links = ('id',
                          'username')


admin.site.register(User, UserAdmin)
