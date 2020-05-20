from django.contrib import admin
from .models import UrlDetails
# Register your models here.

@admin.register(UrlDetails)
class UrlDetailsAdmin(admin.ModelAdmin):
    list_display = ['url', 'title', 'location']
    # list_select_related = ['url']
    list_filter = ['url', 'title', 'location']
    search_fields = ['url', 'title', 'location']
