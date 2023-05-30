from django.contrib import admin
from .models import Reviews

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('username', 'product', 'rate', 'created_at')
    list_display_links = ('username', 'product', 'rate')

admin.site.register(Reviews, ReviewAdmin)