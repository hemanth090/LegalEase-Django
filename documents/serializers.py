"""
API serializers for request validation.
"""

from rest_framework import serializers


class ProcessDocumentSerializer(serializers.Serializer):
    """Serializer for document processing requests."""
    
    file = serializers.FileField(
        help_text="Document file to process (PDF, DOCX, or image)"
    )
    target_language = serializers.CharField(
        max_length=10,
        required=False,
        default='en',
        help_text="Target language code for translation (optional)"
    )
    
    def validate_file(self, value):
        """Validate uploaded file."""
        # Check file size (10MB limit)
        if value.size > 10 * 1024 * 1024:
            raise serializers.ValidationError("File size cannot exceed 10MB")
        
        # Check file type
        allowed_types = [
            'application/pdf',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/msword',
            'image/jpeg',
            'image/png',
            'image/tiff'
        ]
        
        if value.content_type not in allowed_types:
            raise serializers.ValidationError(
                "Unsupported file type. Please upload PDF, DOCX, or image files."
            )
        
        return value