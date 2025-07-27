"""
Main URL configuration for LegalEase project.
"""

from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    """Root API endpoint with basic information."""
    return JsonResponse({
        'message': 'Welcome to LegalEase API',
        'version': '1.0.0',
        'endpoints': {
            'health': '/api/health/',
            'languages': '/api/languages/',
            'process_document': '/api/process-document/',
        },
        'frontend': 'http://localhost:3000',
        'documentation': 'See README.md for API documentation'
    })

urlpatterns = [
    path('', api_root, name='api_root'),
    path('admin/', admin.site.urls),
    path('api/', include('documents.urls')),
]