"""
Minimal models for stateless operation.
No user data or document content is stored.
"""

from django.db import models
from django.utils import timezone


class SystemMetrics(models.Model):
    """
    System performance metrics (no user data).
    """
    timestamp = models.DateTimeField(default=timezone.now)
    endpoint = models.CharField(max_length=50)
    response_time_ms = models.FloatField()
    status_code = models.IntegerField()
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [models.Index(fields=['timestamp', 'endpoint'])]
    
    def __str__(self):
        return f"{self.endpoint} - {self.status_code} ({self.response_time_ms}ms)"


# No other models needed - completely stateless operation