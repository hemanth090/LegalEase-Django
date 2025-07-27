"""
Ultra-optimized AI service for legal document simplification.
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

class AIService:
    """Optimized AI service with caching and connection pooling."""
    
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
    
    def simplify_legal_text(self, text):
        """Optimized legal text simplification with caching."""
        # Check cache first
        cache_key = f"simplified_{hash(text)}"
        cached_result = cache.get(cache_key)
        if cached_result:
            return cached_result
        
        if not self._initialize_groq():
            result = self._get_fallback_response(text)
        else:
            try:
                completion = self._groq_client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": self._get_optimized_prompt()
                        },
                        {
                            "role": "user",
                            "content": f"Explain this legal document:\n\n{text[:4000]}"  # Limit input
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                    temperature=0.3,
                    max_tokens=1500,  # Reduced for faster response
                    timeout=30  # 30 second timeout
                )
                
                result = completion.choices[0].message.content
            except Exception:
                result = self._get_fallback_response(text)
        
        # Cache result for 1 hour
        cache.set(cache_key, result, 3600)
        return result
    
    @lru_cache(maxsize=1)
    def _get_optimized_prompt(self):
        """Cached optimized system prompt."""
        return """You are a legal expert. Explain legal documents in simple terms using this format:

# 📋 Document Summary

## 🔍 Overview
Brief 2-sentence summary

## 👥 Key Parties
Main people/organizations involved

## 📝 Important Terms
Key legal terms explained simply

## 📄 Main Points
- Key clauses in plain English
- Important obligations

## ⚠️ Key Warnings
Critical things to know

## 🎯 Next Steps
What to do next

Use simple language. Be concise."""
    
    def _get_fallback_response(self, text):
        """Optimized fallback response."""
        return f"""# 📋 Document Analysis

## ⚠️ AI Service Unavailable
The AI service is not configured. Configure your Groq API key for detailed analysis.

## 📝 Document Preview
```
{text[:300]}{'...' if len(text) > 300 else ''}
```

## 📄 General Guidance
- Review all terms carefully
- Note dates and obligations
- Consider legal consultation

## 🎯 Recommendation
Configure AI service or consult an attorney."""

# Global singleton instance
ai_service = AIService()

def simplify_legal_text(text):
    """Optimized convenience function."""
    return ai_service.simplify_legal_text(text)