"""
API URL patterns for stateless document processing.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('process-document/', views.process_document, name='process_document'),
    path('languages/', views.get_supported_languages_view, name='supported_languages'),
]