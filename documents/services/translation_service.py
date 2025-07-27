"""
Ultra-optimized translation service with caching and connection pooling.
"""

import logging
from functools import lru_cache
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

# Optimized language list
LANGUAGE_NAMES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'hi': 'Hindi',
    'zh': 'Chinese (Simplified)',
    'ar': 'Arabic',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ja': 'Japanese',
    'it': 'Italian',
    'ko': 'Korean',
    'th': 'Thai',
    'vi': 'Vietnamese',
    'nl': 'Dutch',
    'pl': 'Polish',
    'sv': 'Swedish',
    'da': 'Danish',
    'no': 'Norwegian',
    'fi': 'Finnish'
}

class TranslationService:
    """Optimized translation service with singleton pattern."""
    
    _instance = None
    _groq_client = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.groq_initialized = False
            self.initialized = True
    
    def _initialize_groq(self):
        """Initialize Groq client with connection reuse."""
        if self.groq_initialized:
            return self._groq_client is not None
        
        if not GROQ_AVAILABLE:
            self.groq_initialized = True
            return False
        
        api_key = getattr(settings, 'GROQ_API_KEY', None)
        if not api_key or api_key == 'your_groq_api_key_here':
            self.groq_initialized = True
            return False
        
        try:
            self._groq_client = Groq(api_key=api_key)
        except Exception:
            self._groq_client = None
        
        self.groq_initialized = True
        return self._groq_client is not None
    
    def translate_text(self, text, target_language):
        """Optimized translation with caching."""
        if target_language == 'en':
            return text
        
        # Check cache first
        cache_key = f"translation_{hash(text)}_{target_language}"
        cached_result = cache.get(cache_key)
        if cached_result:
            return cached_result
        
        if not self._initialize_groq():
            result = self._get_mock_translation(target_language)
        else:
            try:
                target_language_name = LANGUAGE_NAMES.get(target_language, target_language)
                
                completion = self._groq_client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": f"Translate to {target_language_name}. Maintain formatting."
                        },
                        {
                            "role": "user",
                            "content": text[:3000]  # Limit input for faster processing
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.2,
                    max_tokens=2000,
                    timeout=25  # 25 second timeout
                )
                
                result = completion.choices[0].message.content
            except Exception:
                result = self._get_mock_translation(target_language)
        
        # Cache result for 2 hours
        cache.set(cache_key, result, 7200)
        return result
    
    @lru_cache(maxsize=20)
    def _get_mock_translation(self, target_language):
        """Cached mock translations."""
        language_name = LANGUAGE_NAMES.get(target_language, target_language)
        
        mock_translations = {
            'es': f"""# 📋 Análisis de Documento

[Traducción de muestra en español]

**Nota**: Configure el servicio con su clave API de Groq para traducción real.

**Idioma**: {language_name}""",
            
            'fr': f"""# 📋 Analyse de Document

[Exemple de traduction française]

**Note**: Configurez le service avec votre clé API Groq pour une vraie traduction.

**Langue**: {language_name}""",
            
            'hi': f"""# 📋 दस्तावेज़ विश्लेषण

[हिंदी अनुवाद नमूना]

**नोट**: वास्तविक अनुवाद के लिए Groq API कुंजी कॉन्फ़िगर करें।

**भाषा**: {language_name}""",
        }
        
        return mock_translations.get(target_language, f"""# 📋 Document Analysis

[Sample translation for {language_name}]

**Note**: Configure Groq API key for real translation.

**Language**: {language_name}""")
    
    @lru_cache(maxsize=1)
    def get_supported_languages(self):
        """Cached supported languages."""
        return LANGUAGE_NAMES.copy()

# Global singleton instance
translation_service = TranslationService()

def translate_text(text, target_language):
    """Optimized convenience function."""
    return translation_service.translate_text(text, target_language)

@lru_cache(maxsize=1)
def get_supported_languages():
    """Cached convenience function."""
    return translation_service.get_supported_languages()