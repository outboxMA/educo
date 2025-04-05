from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date', 'type')
    list_filter = ('type',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    ordering = ('-date',)
