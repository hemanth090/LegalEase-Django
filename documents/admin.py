"""
Admin configuration for system monitoring.
"""

from django.contrib import admin
from .models import SystemMetrics


@admin.register(SystemMetrics)
class SystemMetricsAdmin(admin.ModelAdmin):
    """Admin interface for system performance metrics."""
    
    list_display = ['timestamp', 'endpoint', 'status_code', 'response_time_ms']
    list_filter = ['endpoint', 'status_code', 'timestamp']
    readonly_fields = ['timestamp', 'endpoint', 'response_time_ms', 'status_code']
    ordering = ['-timestamp']
    list_per_page = 50
    
    def has_add_permission(self, request):
        return False  # Metrics are auto-generated
    
    def has_change_permission(self, request, obj=None):
        return False  # Read-only metrics