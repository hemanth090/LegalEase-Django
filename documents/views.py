"""
Ultra-optimized stateless document processing views.
All processing happens in memory with aggressive caching.
"""

import logging
from functools import lru_cache
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.core.cache import cache

from .serializers import ProcessDocumentSerializer
from .services.text_extractor import extract_text_from_file, determine_file_type
from .services.ai_service import simplify_legal_text
from .services.translation_service import translate_text, get_supported_languages

logger = logging.getLogger(__name__)

# Cache supported languages for 1 hour
@lru_cache(maxsize=1)
def get_cached_languages():
    """Cache supported languages to avoid repeated API calls."""
    try:
        return get_supported_languages()
    except Exception as e:
        logger.error(f"Error getting languages: {str(e)}")
        return {
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'hi': 'Hindi'
        }

@cache_page(60 * 15)  # Cache for 15 minutes
def health_check(request):
    """Cached API health check endpoint."""
    return JsonResponse({
        'status': 'healthy',
        'message': 'LegalEase API is operational',
        'version': '1.0.0',
        'timestamp': cache.get('health_timestamp', 'unknown')
    })

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def process_document(request):
    """
    Ultra-optimized document processing with memory management.
    """
    try:
        # Fast validation
        serializer = ProcessDocumentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {'error': 'Invalid request', 'details': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        uploaded_file = serializer.validated_data['file']
        target_language = serializer.validated_data.get('target_language', 'en')
        
        # Quick file type validation
        file_type = determine_file_type(uploaded_file.name, uploaded_file.content_type)
        if file_type == 'unknown':
            return Response(
                {'error': 'Unsupported file type. Please upload PDF, DOCX, or image files.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Process file in memory with size limit
        if uploaded_file.size > 10 * 1024 * 1024:  # 10MB limit
            return Response(
                {'error': 'File too large. Maximum size is 10MB.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        file_content = uploaded_file.read()
        
        # Extract text with timeout protection
        extracted_text = extract_text_from_file(file_content, file_type)
        if not extracted_text or len(extracted_text.strip()) < 10:
            return Response(
                {'error': 'Could not extract meaningful text from the document.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Limit text size for processing
        if len(extracted_text) > 50000:  # 50k chars limit
            extracted_text = extracted_text[:50000] + "\n\n[Text truncated for processing]"
        
        # Simplify legal text
        simplified_text = simplify_legal_text(extracted_text)
        
        # Translate if requested (with caching)
        translated_text = None
        if target_language != 'en':
            cache_key = f"translation_{hash(simplified_text)}_{target_language}"
            translated_text = cache.get(cache_key)
            
            if not translated_text:
                translated_text = translate_text(simplified_text, target_language)
                if translated_text:
                    # Cache translation for 1 hour
                    cache.set(cache_key, translated_text, 3600)
        
        # Prepare optimized response
        response_data = {
            'success': True,
            'file_info': {
                'name': uploaded_file.name,
                'type': file_type,
                'size_mb': round(uploaded_file.size / (1024 * 1024), 2)
            },
            'results': {
                'original_text': extracted_text,
                'simplified_text': simplified_text,
            }
        }
        
        if translated_text:
            response_data['results']['translated_text'] = translated_text
            response_data['target_language'] = target_language
        
        return Response(response_data, status=status.HTTP_200_OK)
        
    except Exception as e:
        logger.error(f"Processing error: {str(e)}")
        return Response(
            {'error': f'Processing failed: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
@cache_page(60 * 60)  # Cache for 1 hour
@vary_on_headers('Accept-Language')
def get_supported_languages_view(request):
    """Cached supported languages endpoint."""
    try:
        languages = get_cached_languages()
        return Response({
            'success': True,
            'languages': languages,
            'count': len(languages)
        })
    except Exception as e:
        logger.error(f"Error getting languages: {str(e)}")
        return Response(
            {'error': 'Failed to get supported languages'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )