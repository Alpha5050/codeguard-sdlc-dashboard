from django.contrib import admin
from .models import SecurityFinding


@admin.register(SecurityFinding)
class SecurityFindingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'severity',
        'status',
        'assigned_to',
        'created_at',
    )

    list_filter = ('category', 'severity', 'status')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.
